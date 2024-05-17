import os

try:
    if os.name == "nt":
        from ansys.stk.core.stkdesktop import STKDesktop
    from ansys.stk.core.stkobjects import *
    from ansys.stk.core.stkobjects.aviator import *
    from ansys.stk.core.utilities.colors import *
except:
    print("Failed to import stk modules. Make sure you have installed the STK Python API wheel (agi.stk<..ver..>-py3-none-any.whl) from the STK Install bin directory")

### Quick tip: If you would like to use a more detailed carrier ship
### download the CVN-72 model from support.agi.com/3d-models and
### place it into the following location before running the script: 
### <STK Install Directory>\STKData\VO\Models\Sea

############################################################################
# Setup and Create the Scenario
############################################################################

print('...Opening the application')

if os.name == "nt":
    try:
        # Grab an existing instance of STK
        stkUiApplication = STKDesktop.attach_to_application()
        stkRoot = stkUiApplication.root
        checkempty = stkRoot.children.count
        if checkempty == 0:
            # If a Scenario is not open, create a new scenario
            stkUiApplication.visible = True
        else:
            # If a Scenario is open and has objects in it, launch new instance of STK 12
            stkUiApplication = STKDesktop.start_application(visible=True, userControl=True)
            stkRoot = stkUiApplication.root
    except Exception:
        # STK is not running, launch new instance of STK 12 and grab it
        stkUiApplication = STKDesktop.start_application(visible=True, userControl=True)
        stkRoot = stkUiApplication.root
else:
    print("Automation samples only work on windows with the desktop application, see Custom Applications for STK Engine examples.")
    quit()
    
stkRoot.new_scenario('Aviator_Carrier_Landing_Example')

print('...Creating new scenario')

# Set scenario time interval
scenario = stkRoot.current_scenario
scenario.SetTimePeriod('20 Jan 2020 17:00:00.000', '+2 hours') # times are UTCG

# Reset animation time to new scenario start time
stkRoot.rewind()

# Set scenario global reference to MSL
scenario.VO.SurfaceReference = SURFACE_REFERENCE.MEAN_SEA_LEVEL

if os.name == "nt":
    # Maximize application window
    stkRoot.execute_command('Application / Raise')
    stkRoot.execute_command('Application / Maximize')

    # Maximize 3D window
    stkRoot.execute_command('Window3D * Maximize')


############################################################################
# Create Facility to Represent the Oceana Naval Air Station (KNTU)
############################################################################

print('...Adding Oceana Naval Air Station')

facilityKntu = scenario.children.new(STK_OBJECT_TYPE.eFacility, 'OCEANA_NAS__APOLLO_SOUCEK_FIELD')

# Set facility postiion
facilityKntu.UseTerrain = True
facilityKntu.Position.AssignGeodetic(36.822744, -76.031892, 0.0) # setting alt to zero will place it on terrain

# Set facility color
facilityKntu.Graphics.Color = Colors.White


############################################################################
# Create Ship to Represent the USS Abraham Lincoln (CVN-72)
############################################################################

print('...Adding CVN-72 carrier ship')

shipCvn72 = scenario.children.new(STK_OBJECT_TYPE.eShip, 'CVN-72')

# Set route properties
shipCvn72.SetRouteType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
shipCvn72.Route.SetAltitudeRefType(VEHICLE_ALTITUDE_REFERENCE.WAYPOINT_ALTITUDE_REFERENCE_TERRAIN)
shipCvn72.Route.AltitudeRef.Granularity = 1 # km

# Set waypoints
waypoint1 = shipCvn72.Route.Waypoints.Add()
waypoint1.Latitude = 36.64988281 # deg
waypoint1.Longitude = -75.11230361 # deg
waypoint1.Speed = 0.01543333 # km/s
waypoint1.Altitude = 0 # km
waypoint2 = shipCvn72.Route.Waypoints.Add()
waypoint2.Latitude = 36.63713768 # deg
waypoint2.Longitude = -74.87339587 # deg
waypoint2.Speed = 0.01543333 # km/s
waypoint2.Altitude = 0 # km
waypoint3 = shipCvn72.Route.Waypoints.Add()
waypoint3.Latitude = 36.65454874 # deg
waypoint3.Longitude = -75.29117133 # deg
waypoint3.Speed = 0.01543333 # km/s
waypoint3.Altitude = 0 # km

# Set display properties
shipCvn72.Graphics.Attributes.Color = Colors.Cyan
shipCvn72.Graphics.Attributes.Line.Width = LINE_WIDTH.WIDTH3 # medium thickness.

# Set ship model
try:
    # Insert CVN-72 model if available
    shipCvn72.VO.Model.ModelData.Filename = os.path.join('STKData', 'VO', 'Models', 'Sea', 'cvn-72.glb')
except:
    # Insert default carrier model from STK install folder
    shipCvn72.VO.Model.ModelData.Filename = os.path.join('STKData', 'VO', 'Models', 'Sea', 'aircraft-carrier.glb')
    shipCvn72.VO.Offsets.Translational.Enable = True;
    shipCvn72.VO.Offsets.Translational.Z = 0.02; # km

# Propagate ship
shipCvn72.Route.Propagate()

if os.name == "nt":
    # Position 3D window near ship
    stkRoot.execute_command('VO * ViewFromTo Normal From Ship/CVN-72') # zoom to ship
    stkRoot.execute_command('VO * ViewerPosition 20 115 150000') # set view position


############################################################################
# Create Lead Hornet Aircraft to Perform Carrier Landing
############################################################################

print('...Creating lead hornet aircraft')

aircraftHornetLead = scenario.children.new(STK_OBJECT_TYPE.eAircraft, 'Hornet_Flight_Lead')

# Set propagator to Aviator
aircraftHornetLead.SetRouteType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_AVIATOR)

# Grab the Aviator Propagator
avtrPropHornetLead = aircraftHornetLead.Route.AvtrPropagator

# Grab the Aviator catalog. This handle can be used for later aircraft too.
catalog = avtrPropHornetLead.AvtrCatalog

# Grab the aircraft models from the catalog
acModels = catalog.AircraftCategory.AircraftModels

# If a copy of the Basic Fighter aircraft model already exists, remove it
if acModels.Contains('Basic Fighter'):
    basicFighter = acModels.GetAircraft('Basic Fighter')
else:
    print('...Basic Fighter aircraft model cannot be found.')

# Grab the mission
avtrMissionHornetLead = avtrPropHornetLead.AvtrMission

# Set the aircraft model to Basic Fighter Copy
avtrMissionHornetLead.Vehicle = basicFighter

# From the mission grab the phase collection
phasesHornetLead = avtrMissionHornetLead.Phases

# Get the first phase
phaseHornetLead = phasesHornetLead[0]

# Get the procedure collection
proceduresHornetLead = phaseHornetLead.Procedures

# Set display properties
aircraftHornetLead.Graphics.Attributes.Color = Colors.Yellow
aircraftHornetLead.Graphics.Attributes.Line.Width = LINE_WIDTH.WIDTH3 # medium thickness.

##  Get the runways from the catalog

# Get the runway category
runwayCategory = avtrPropHornetLead.AvtrCatalog.RunwayCategory

# Set the ARINC runways to look at the installed sample
installDir = stkRoot.execute_command('GetDirectory / STKHome')[0]
runwayCategory.ARINC424Runways.MasterDataFilepath = os.path.join(installDir, 'Data', 'Resources', 'stktraining', 'samples', 'FAANFD18')

# Get the list of runways
runwaysARINC424 = runwayCategory.ARINC424Runways
runwayList = runwaysARINC424.ChildNames

# Grab Oceana NAS from runways
runwayNameOceana = 'OCEANA NAS /APOLLO SOUCEK FIEL 05R 23L'
if runwaysARINC424.Contains(runwayNameOceana):
    oceana = runwaysARINC424.GetARINC424Item(runwayNameOceana)
else:
    print('...Runway ' + runwayNameOceana + ' does not exist in catalog.')


### Add a Takeoff Procedure

print('...Lead hornet - adding takeoff procedure')

# Add a takeoff procedure from a runway
takeoffHornetLead = proceduresHornetLead.Add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)

## Set the site properties

# Get the site
oceanaRunway = takeoffHornetLead.Site

# Copy the Oceana runway
oceanaRunway.CopyFromCatalog(oceana)
oceanaRunway.Name = runwayNameOceana

## Set the procedure properties

# Get the runway heading options
runwayOptionsHornetLead = takeoffHornetLead.RunwayHeadingOptions

# Set it to low end
runwayOptionsHornetLead.RunwayMode = RUNWAY_HIGH_LOW_END.LOW_END

# Set the takeoff to normal
takeoffHornetLead.TakeoffMode = TAKEOFF_MODE.TAKEOFF_NORMAL

# Get the interface for a normal takeoff
normalTakeoffHornetLead = takeoffHornetLead.ModeAsNormal

# Get the angle and terrain option
normalTakeoffHornetLead.TakeoffClimbAngle = 3 # deg
normalTakeoffHornetLead.DepartureAltitude = 500 # ft
normalTakeoffHornetLead.RunwayAltitudeOffset = 0 # ft
normalTakeoffHornetLead.UseRunwayTerrain = True


### Add an Enroute Procedure to Begin Approach to Ship

print('...Lead hornet - adding enroute procedure to approach ship')

enrouteHornetLead = proceduresHornetLead.Add(SITE_TYPE.SITE_STK_OBJECT_WAYPOINT, PROCEDURE_TYPE.PROC_ENROUTE)

## Set the site properties
enrouteHornetLeadSite = enrouteHornetLead.Site

# Link to ship object
enrouteHornetLeadSite.ObjectName = 'Ship/CVN-72'

# Set waypoint time to scenario start time
enrouteHornetLeadSite.WaypointTime = scenario.StartTime

# Set Offset mode and bearing/range values
enrouteHornetLeadSite.OffsetMode = STK_OBJECT_WAYPOINT_OFFSET_MODE.OFFSET_RELATIVE_BEARING_RANGE
enrouteHornetLeadSite.Bearing = 180 # deg
enrouteHornetLeadSite.Range = 40 # nm

## Set the procedure properties

# Set the altitude options
enrouteHornetLead.AltitudeMSLOptions.UseDefaultCruiseAltitude = False
enrouteHornetLead.AltitudeMSLOptions.MSLAltitude = 20000 # ft

# Set the navigation options
enrouteHornetLead.NavigationOptions.NavMode = POINT_TO_POINT_MODE.ARRIVE_ON_COURSE
enrouteHornetLead.NavigationOptions.ArriveOnCourse = 135 # deg


### Add a 2nd Enroute Procedure to "Enter the Stack"

print('...Lead hornet - adding enroute procedure to enter stack')

enroute2HornetLead = proceduresHornetLead.Add(SITE_TYPE.SITE_STK_OBJECT_WAYPOINT, PROCEDURE_TYPE.PROC_ENROUTE)

## Set the site properties
enroute2HornetLeadSite = enroute2HornetLead.Site

# Link to ship object
enroute2HornetLeadSite.ObjectName = 'Ship/CVN-72'

# Set waypoint time to scenario start time
enroute2HornetLeadSite.WaypointTime = '20 Jan 2020 17:09:06.858' # UTCG

# Set Offset mode and bearing/range values
enroute2HornetLeadSite.OffsetMode = STK_OBJECT_WAYPOINT_OFFSET_MODE.OFFSET_RELATIVE_BEARING_RANGE
enroute2HornetLeadSite.Bearing = 180 # deg
enroute2HornetLeadSite.Range = 10 # nm

## Set the procedure properties

# Set the procedure name
enroute2HornetLead.Name = 'Enter the Stack'

# Set the altitude options
enroute2HornetLead.AltitudeMSLOptions.UseDefaultCruiseAltitude = False
enroute2HornetLead.AltitudeMSLOptions.MSLAltitude = 10000 # ft

# Set the navigation options
enroute2HornetLead.NavigationOptions.NavMode = POINT_TO_POINT_MODE.ARRIVE_ON_COURSE_FOR_NEXT

# Set the enroute cruise airspeed options
enroute2HornetLead.EnrouteCruiseAirspeedOptions.CruiseSpeedType = CRUISE_SPEED.MAX_ENDURANCE_AIRSPEED


### Create a New Mission Phase for StationKeeping

phase2HornetLead = avtrMissionHornetLead.Phases.Add()
phase2HornetLead.Name = 'StationKeeping'

# Get procedures for new phase
procedures2HornetLead = phase2HornetLead.Procedures


### Add a Basic Maneuver Procedure to "Enter Case 1 Marshall"

print('...Lead hornet - adding maneuever to enter Case I Marshall')

# Add a Basic Maneuver procedure from the end of the previous procedure
basicManeuverHornetLead = procedures2HornetLead.Add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER)

## Set the procedure properties

# Set procedure name
basicManeuverHornetLead.Name = 'Case I Marshall'

## Set the horizontal/navigation strategy
basicManeuverHornetLead.NavigationStrategyType = 'Stationkeeping'

# Get the navigation interface
stationkeepingNavHornetLead = basicManeuverHornetLead.Navigation

# Set stationkeeping target
stationkeepingNavHornetLead.TargetName = 'Ship/CVN-72'

# Set station options
stationkeepingNavHornetLead.RelBearing = -90 # deg
stationkeepingNavHornetLead.RelRange = 2.7 # nm
stationkeepingNavHornetLead.DesiredRadius = 2.5 # nm
stationkeepingNavHornetLead.TurnDirection = TURN_DIRECTION.TURN_LEFT

# Set stop condition options
stationkeepingNavHornetLead.StopCondition = STATIONKEEPING_STOP_CONDITION.STOP_AFTER_TURN_COUNT
stationkeepingNavHornetLead.StopAfterTurnCount = 5
stationkeepingNavHornetLead.UseRelativeCourse = True
stationkeepingNavHornetLead.StopCourse = -180 # deg

## Set the vertical/profile strategy
basicManeuverHornetLead.ProfileStrategyType = 'Autopilot - Vertical Plane'

# Get the profile interface
autoProfileHornetLead = basicManeuverHornetLead.Profile

# Set the altitude options
autoProfileHornetLead.AltitudeMode = AUTOPILOT_ALTITUDE_MODE.AUTOPILOT_SPECIFY_ALTITUDE
autoProfileHornetLead.AbsoluteAltitude = 2000 # ft
autoProfileHornetLead.AltitudeControlMode = AUTOPILOT_ALTITUDE_CONTROL_MODE.AUTOPILOT_ALTITUDE_RATE
autoProfileHornetLead.ControlAltitudeRateValue = 2000 # ft/min
autoProfileHornetLead.ControlLimitMode = PERF_MODEL_OVERRIDE.OVERRIDE
autoProfileHornetLead.MaxPitchRate = 10 # deg/s
autoProfileHornetLead.DampingRatio = 2

# Set the airspeed options
autoProfileHornetLead.AirspeedOptions.AirspeedMode = BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_MAX_ENDURANCE_AIRSPEED
autoProfileHornetLead.AirspeedOptions.MinSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED
autoProfileHornetLead.AirspeedOptions.MaxSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED

## Set the attitude/performance/fuel options
basicManeuverHornetLead.FlightMode = PHASE_OF_FLIGHT.FLIGHT_PHASE_CRUISE
basicManeuverHornetLead.FuelFlowType = BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_CRUISE

## Set the basic stop conditions
basicManeuverHornetLead.UseStopFuelState = True
basicManeuverHornetLead.StopFuelState = 2000 # lb
basicManeuverHornetLead.UseMaxTimeOfFlight = False
basicManeuverHornetLead.UseMaxDownrange = True
basicManeuverHornetLead.MaxDownrange = 500 # nm

basicManeuverHornetLead.AltitudeLimitMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_ERROR
basicManeuverHornetLead.TerrainImpactMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_CONTINUE


### Add a Basic Maneuver to "Enter Break"

print('...Lead hornet - adding maneuever to enter break')

# Add a Basic Maneuver procedure from the end of the previous procedure
basicManeuver2HornetLead = procedures2HornetLead.Add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER)

# Set the site name
basicManeuver2HornetLead.Site.Name = 'Mother'

## Set the procedure properties

# Set procedure name
basicManeuver2HornetLead.Name = 'Enter Break'

## Set the horizontal/navigation strategy
basicManeuver2HornetLead.NavigationStrategyType = 'Relative Course'

# Get the navigation interface
relCourse = basicManeuver2HornetLead.Navigation

# Set the target
relCourse.TargetName = 'Ship/CVN-72'

# Set relative or true course option
relCourse.UseRelativeCourse = True
relCourse.Course = 0 # deg

# Set the anchor offset
relCourse.InTrack = 1 # nm
relCourse.CrossTrack = 0 # nm

# Set other options
relCourse.UseApproachTurnMode = True

# Set closure mode
relCourse.ClosureMode = CLOSURE_MODE.HOBS
relCourse.DownrangeOffset = 0 # nm
relCourse.HOBSMaxAngle =  90 # deg

## Set the vertical/profile strategy
basicManeuver2HornetLead.ProfileStrategyType = 'Autopilot - Vertical Plane'

# Get the profile interface
autoProfile2HornetLead = basicManeuver2HornetLead.Profile

# Set the altitude options
autoProfile2HornetLead.AltitudeMode = AUTOPILOT_ALTITUDE_MODE.AUTOPILOT_SPECIFY_ALTITUDE
autoProfile2HornetLead.AbsoluteAltitude = 800 # ft
autoProfile2HornetLead.AltitudeControlMode = AUTOPILOT_ALTITUDE_CONTROL_MODE.AUTOPILOT_ALTITUDE_RATE
autoProfile2HornetLead.ControlAltitudeRateValue = 2000 # ft/min
autoProfile2HornetLead.ControlLimitMode = PERF_MODEL_OVERRIDE.OVERRIDE
autoProfile2HornetLead.MaxPitchRate = 10 # deg/s
autoProfile2HornetLead.DampingRatio = 2

# Set the airspeed options
autoProfile2HornetLead.AirspeedOptions.AirspeedMode = BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_SPECIFIED_AIRSPEED
autoProfile2HornetLead.AirspeedOptions.SpecifiedAirspeedType = AIRSPEED_TYPE.CAS
autoProfile2HornetLead.AirspeedOptions.SpecifiedAirspeed = 350 # nm/hr
autoProfile2HornetLead.AirspeedOptions.MinSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED
autoProfile2HornetLead.AirspeedOptions.MaxSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED

## Set the attitude/performance/fuel options
basicManeuver2HornetLead.FlightMode = PHASE_OF_FLIGHT.FLIGHT_PHASE_CRUISE
basicManeuver2HornetLead.FuelFlowType = BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_CRUISE

## Set the basic stop conditions
basicManeuver2HornetLead.UseStopFuelState = True
basicManeuver2HornetLead.StopFuelState = 0 # lb
basicManeuver2HornetLead.UseMaxTimeOfFlight = False
basicManeuver2HornetLead.UseMaxDownrange = True
basicManeuver2HornetLead.MaxDownrange = 100 # nm

basicManeuver2HornetLead.AltitudeLimitMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_ERROR
basicManeuver2HornetLead.TerrainImpactMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_CONTINUE


### Add a Basic Maneuver Procedure to "Break"

print('...Lead hornet - adding maneuever to break')

# Add a Basic Maneuver procedure from the end of the previous procedure
basicManeuver3HornetLead = procedures2HornetLead.Add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER)

## Set the procedure properties

# Set procedure name
basicManeuver3HornetLead.Name = 'Break'

## Set the horizontal/navigation strategy
basicManeuver3HornetLead.NavigationStrategyType = 'Relative Course'

# Get the navigation interface
relCourse2 = basicManeuver3HornetLead.Navigation

# Set the target
relCourse2.TargetName = 'Ship/CVN-72'

# Set relative or true course option
relCourse2.UseRelativeCourse = True
relCourse2.Course = 180 # deg

# Set the anchor offset
relCourse2.InTrack = 0 # nm
relCourse2.CrossTrack = -1.3 # nm

# Set other options
relCourse2.UseApproachTurnMode = True

# Set maneuver factor
relCourse2.ManeuverFactor = 1.00 # aggressive

# Set control limit
relCourse2.SetControlLimit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_TURN_RATE, 29.9725) # deg/s

# Set closure mode
relCourse2.ClosureMode = CLOSURE_MODE.HOBS
relCourse2.DownrangeOffset = 0 # nm
relCourse2.HOBSMaxAngle =  90 # deg

## Set the vertical/profile strategy
basicManeuver3HornetLead.ProfileStrategyType = 'Autopilot - Vertical Plane'

# Get the profile interface
autoProfile3HornetLead = basicManeuver3HornetLead.Profile

# Set the altitude options
autoProfile3HornetLead.AltitudeMode = 1
autoProfile3HornetLead.AbsoluteAltitude = 600 # ft
autoProfile3HornetLead.AltitudeControlMode = AUTOPILOT_ALTITUDE_CONTROL_MODE.AUTOPILOT_ALTITUDE_RATE
autoProfile3HornetLead.ControlAltitudeRateValue = 2000 # ft/min
autoProfile3HornetLead.ControlLimitMode = 1
autoProfile3HornetLead.MaxPitchRate = 10 # deg/s
autoProfile3HornetLead.DampingRatio = 2

# Set the airspeed options
autoProfile3HornetLead.AirspeedOptions.AirspeedMode = BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_SPECIFIED_AIRSPEED
autoProfile3HornetLead.AirspeedOptions.SpecifiedAirspeedType = AIRSPEED_TYPE.CAS
autoProfile3HornetLead.AirspeedOptions.SpecifiedAirspeed = 145 # nm/hr
autoProfile3HornetLead.AirspeedOptions.SpecifiedAccelDecelMode = PERF_MODEL_OVERRIDE.OVERRIDE
autoProfile3HornetLead.AirspeedOptions.SpecifiedAccelDecelG = 0.3 # G's
autoProfile3HornetLead.AirspeedOptions.MinSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED
autoProfile3HornetLead.AirspeedOptions.MaxSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED

## Set the attitude/performance/fuel options
basicManeuver3HornetLead.FlightMode = PHASE_OF_FLIGHT.FLIGHT_PHASE_CRUISE
basicManeuver3HornetLead.FuelFlowType = BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_CRUISE

## Set the basic stop conditions
basicManeuver3HornetLead.UseStopFuelState = True
basicManeuver3HornetLead.StopFuelState = 0 # lb
basicManeuver3HornetLead.UseMaxTimeOfFlight = False
basicManeuver3HornetLead.UseMaxDownrange = True
basicManeuver3HornetLead.MaxDownrange = 50 # nm

basicManeuver3HornetLead.AltitudeLimitMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_ERROR
basicManeuver3HornetLead.TerrainImpactMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_CONTINUE


### Add a Basic Maneuver Procedure to "Recover" (Land on Ship)

print('...Lead hornet - adding maneuever to recover')

# Add a Basic Maneuver procedure from the end of the previous procedure
basicManeuver4HornetLead = procedures2HornetLead.Add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER)

## Set the procedure properties

# Set procedure name
basicManeuver4HornetLead.Name = 'Recover'

## Set the horizontal/navigation strategy
basicManeuver4HornetLead.NavigationStrategyType = 'Relative Course'

# Get the navigation interface
relCourse3 = basicManeuver4HornetLead.Navigation

# Set the target
relCourse3.TargetName = 'Ship/CVN-72'

# Set relative or true course option
relCourse3.UseRelativeCourse = True
relCourse3.Course = -9.0 # deg

# Set the anchor offset
stkRoot.unit_preferences['AviatorDistance'].set_current_unit('ft')
relCourse3.InTrack = -850 # ft
relCourse3.CrossTrack = 75 # ft
stkRoot.unit_preferences['AviatorDistance'].set_current_unit('nm')

# Set other options
relCourse3.UseApproachTurnMode = True

# Set closure mode
relCourse3.ClosureMode = CLOSURE_MODE.HOBS
relCourse3.DownrangeOffset = 0.1 # nm
relCourse3.HOBSMaxAngle =  90 # deg

## Set the vertical/profile strategy
basicManeuver4HornetLead.ProfileStrategyType = 'Relative Flight Path Angle'

# Get the profile interface
relFpa = basicManeuver4HornetLead.Profile

# Set FPA and anchor alt offset
relFpa.FPA = -3.5 # deg
relFpa.AnchorAltOffset = 100 # ft

# Set control limit
relFpa.SetControlLimit(PROFILE_CONTROL_LIMIT.PROFILE_PITCH_RATE, 10) # deg/s

# Set airspeed options
relFpa.AirspeedOptions.AirspeedMode = BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_CURRENT_AIRSPEED
relFpa.AirspeedOptions.MaintainAirspeedType = AIRSPEED_TYPE.TAS
relFpa.AirspeedOptions.MinSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED
relFpa.AirspeedOptions.MaxSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED

## Set the attitude/performance/fuel options
basicManeuver4HornetLead.FlightMode = PHASE_OF_FLIGHT.FLIGHT_PHASE_CRUISE
basicManeuver4HornetLead.FuelFlowType = BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_CRUISE

## Set the basic stop conditions
basicManeuver4HornetLead.UseStopFuelState = True
basicManeuver4HornetLead.StopFuelState = 0 # lb
basicManeuver4HornetLead.UseMaxTimeOfFlight = False
basicManeuver4HornetLead.UseMaxDownrange = True
basicManeuver4HornetLead.MaxDownrange = 50 # nm

basicManeuver4HornetLead.AltitudeLimitMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_ERROR
basicManeuver4HornetLead.TerrainImpactMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_CONTINUE

# Propagate aircraft
avtrPropHornetLead.Propagate()


############################################################################
# Create Wingman Hornet Aircraft to Fly Formation with Lead
############################################################################

print('...Creating wingman hornet aircraft')

aircraftHornetWing = scenario.children.new(STK_OBJECT_TYPE.eAircraft, 'Hornet_Flight_Wing')

# Set propagator to Aviator
aircraftHornetWing.SetRouteType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_AVIATOR)

# Grab the Aviator Propagator
avtrPropHornetWing = aircraftHornetWing.Route.AvtrPropagator

# Grab the mission
avtrMissionHornetWing = avtrPropHornetWing.AvtrMission

# Set the aircraft model to Basic Fighter Copy
avtrMissionHornetWing.Vehicle = basicFighter

# From the mission grab the phase collection
phasesHornetWing = avtrMissionHornetWing.Phases

# Get the first phase
phaseHornetWing = phasesHornetWing[0]

# Get the procedure collection
proceduresHornetWing = phaseHornetWing.Procedures

# Set display properties
aircraftHornetWing.Graphics.Attributes.Color = Colors.Magenta
aircraftHornetWing.Graphics.Attributes.Line.Width = LINE_WIDTH.WIDTH3 # medium thickness


### Add an Enroute Procedure to Begin Flying to Lead

# Aircraft starts at a waypoint south of the lead aircraft, already flying.

print('...Wing hornet - adding enroute procedure to approach Lead hornet')

enrouteHornetWing = proceduresHornetWing.Add(SITE_TYPE.SITE_WAYPOINT, PROCEDURE_TYPE.PROC_ENROUTE)

## Set the site properties
enrouteHornetWingSite = enrouteHornetWing.Site
enrouteHornetWingSite.Name = 'Waypoint'
enrouteHornetWingSite.Latitude = 36.3174 # deg
enrouteHornetWingSite.Longitude = -75.4974 # deg

## Set the procedure properties

# Set the altitude options
enrouteHornetWing.AltitudeMSLOptions.UseDefaultCruiseAltitude = True

# Set the navigation options
enrouteHornetWing.NavigationOptions.NavMode = POINT_TO_POINT_MODE.ARRIVE_ON_COURSE
enrouteHornetWing.NavigationOptions.ArriveOnCourse = 340.691 # deg


### Add a Basic Maneuver Procedure to "Intercept Leader"

print('...Wing hornet - adding maneuver to intercept Lead hornet')

# Add a Basic Maneuver procedure from the end of the previous procedure
basicManeuverHornetWing = proceduresHornetWing.Add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER)

## Set the procedure properties

# Set procedure name
basicManeuverHornetWing.Name = 'Intercept Leader';

# Set the horizontal/navigation strategy
basicManeuverHornetWing.NavigationStrategyType = 'Relative Bearing';

# Get the navigation interface
relBearing = basicManeuverHornetWing.Navigation;

# Set the target
relBearing.TargetName = 'Aircraft/Hornet_Flight_Lead';

# Set relative bearing values
relBearing.RelBearing = -20; # deg
relBearing.MinRange = 15; # nm

# Set control limits
relBearing.SetControlLimit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_USE_ACCEL_PERF_MODEL, 0)

## Set the vertical/profile strategy
basicManeuverHornetWing.ProfileStrategyType = 'Cruise Profile';

# Get the profile interface
cruiseProfileHornetWing = basicManeuverHornetWing.Profile;

# Set the reference frame
cruiseProfileHornetWing.ReferenceFrame = BASIC_MANEUVER_REFERENCE_FRAME.EARTH_FRAME

# Set the altitude options
cruiseProfileHornetWing.RequestedAltitude = 18000; # ft

# Set cruise airspeed
cruiseProfileHornetWing.CruiseAirspeedOptions.CruiseSpeedType = CRUISE_SPEED.MAX_RANGE_AIRSPEED

## Set the attitude/performance/fuel options
basicManeuverHornetWing.FlightMode = PHASE_OF_FLIGHT.FLIGHT_PHASE_CRUISE
basicManeuverHornetWing.FuelFlowType = BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_CRUISE

## Set the basic stop conditions
basicManeuverHornetWing.UseStopFuelState = True;
basicManeuverHornetWing.StopFuelState = 0.0;
basicManeuverHornetWing.UseMaxTimeOfFlight = False;
basicManeuverHornetWing.UseMaxDownrange = False;

basicManeuverHornetWing.AltitudeLimitMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_ERROR
basicManeuverHornetWing.TerrainImpactMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_CONTINUE


### Add a Basic Maneuver Procedure to "Fly Formation to Marshall"

print('...Wing hornet - adding maneuver to fly in formation to Marshall')

# Add a Basic Maneuver procedure from the end of the previous procedure
basicManeuverHornetWing = proceduresHornetWing.Add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER)

## Set the procedure properties

# Set procedure name
basicManeuverHornetWing.Name = 'Fly Formation to Marshall'

## Set the horizontal/navigation strategy
basicManeuverHornetWing.NavigationStrategyType = 'Rendezvous/Formation'

# Get the navigation interface
rendezvousForm = basicManeuverHornetWing.Navigation

# Set the cooperative target
rendezvousForm.TargetName = 'Aircraft/Hornet_Flight_Lead'

# Set the position options
rendezvousForm.RelativeBearing = 135 # deg
rendezvousForm.RelativeRange = 0.25 # nm
rendezvousForm.AltitudeSplit = 100 # ft

# Set the maneuver factor
rendezvousForm.ManeuverFactor = 0.8;

# Enable counter turn logic
rendezvousForm.UseCounterTurnLogic = True;

# Set the collision avoidance logic
rendezvousForm.SetCPA(True,152.4) # nm

# Set the airspeed control options
rendezvousForm.MaxSpeedAdvantage = 75 # nm/hr

# Set the rendezvous stop condition
rendezvousForm.StopCondition = RENDEZVOUS_STOP_CONDITION.STOP_AFTER_TARGET_CURRENT_PHASE

## Set the vertical/profile strategy
# Profile settings are copied from the Navigation settings when using 'Rendezvous/Formation' as the nav mode.

## Set the attitude/performance/fuel options
basicManeuverHornetWing.FlightMode = PHASE_OF_FLIGHT.FLIGHT_PHASE_CRUISE
basicManeuverHornetWing.FuelFlowType = BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_CRUISE

## Set the basic stop conditions
basicManeuverHornetWing.UseStopFuelState = False
basicManeuverHornetWing.UseMaxTimeOfFlight = False
basicManeuverHornetWing.UseMaxDownrange = True
basicManeuverHornetWing.MaxDownrange = 500 # nm

basicManeuverHornetWing.AltitudeLimitMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_ERROR
basicManeuverHornetWing.TerrainImpactMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_CONTINUE


### Add a Basic Maneuver Procedure to "Split - Marshall - 3 Kft"

print('...Wing hornet - adding maneuver to fly Marshall at 3 Kft split from Lead hornet')

# Add a Basic Maneuver procedure from the end of the previous procedure
basicManeuver2HornetWing = proceduresHornetWing.Add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER)

## Set the procedure properties

# Set procedure name
basicManeuver2HornetWing.Name = 'Split - Marshall - 3 Kft'

## Set the horizontal/navigation strategy
basicManeuver2HornetWing.NavigationStrategyType = 'Stationkeeping'

# Get the navigation interface
stationkeepingNavHornetWing = basicManeuver2HornetWing.Navigation

# Set stationkeeping target
stationkeepingNavHornetWing.TargetName = 'Ship/CVN-72'

# Set station options
stationkeepingNavHornetWing.RelBearing = -90 # deg
stationkeepingNavHornetWing.RelRange = 2.7 # nm
stationkeepingNavHornetWing.DesiredRadius = 2.5 # nm
stationkeepingNavHornetWing.TurnDirection = TURN_DIRECTION.TURN_LEFT

# Set stop condition options
stationkeepingNavHornetWing.StopCondition = STATIONKEEPING_STOP_CONDITION.STOP_AFTER_TURN_COUNT
stationkeepingNavHornetWing.StopAfterTurnCount = 5
stationkeepingNavHornetWing.UseRelativeCourse = True
stationkeepingNavHornetWing.StopCourse = -180 # deg

## Set the vertical/profile strategy
basicManeuver2HornetWing.ProfileStrategyType = 'Autopilot - Vertical Plane'

# Get the profile interface
autoProfileHornetWing = basicManeuver2HornetWing.Profile

# Set the altitude options
autoProfileHornetWing.AltitudeMode = AUTOPILOT_ALTITUDE_MODE.AUTOPILOT_SPECIFY_ALTITUDE
autoProfileHornetWing.AbsoluteAltitude = 3000 # ft
autoProfileHornetWing.AltitudeControlMode = 0
autoProfileHornetWing.ControlAltitudeRateValue = 2000 # ft/min
autoProfileHornetWing.ControlLimitMode = 1
autoProfileHornetWing.MaxPitchRate = 10 # deg/s
autoProfileHornetWing.DampingRatio = 2

# Set the airspeed options
autoProfileHornetWing.AirspeedOptions.AirspeedMode = 3
autoProfileHornetWing.AirspeedOptions.MinSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED
autoProfileHornetWing.AirspeedOptions.MaxSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED

## Set the attitude/performance/fuel options
basicManeuver2HornetWing.FlightMode = PHASE_OF_FLIGHT.FLIGHT_PHASE_CRUISE
basicManeuver2HornetWing.FuelFlowType = BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_CRUISE

## Set the basic stop conditions
basicManeuver2HornetWing.UseStopFuelState = False
basicManeuver2HornetWing.UseMaxTimeOfFlight = False
basicManeuver2HornetWing.UseMaxDownrange = True
basicManeuver2HornetWing.MaxDownrange = 500 # nm

basicManeuver2HornetWing.AltitudeLimitMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_ERROR
basicManeuver2HornetWing.TerrainImpactMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_CONTINUE


### Add a Basic Maneuver Procedure to "Marshall - Step Down - 2 Kft"

print('...Wing hornet - adding maneuver to fly Marshall stepped down to 2 Kft')

# Add a Basic Maneuver procedure from the end of the previous procedure
basicManeuver3HornetWing = proceduresHornetWing.Add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER)

## Set the procedure properties

# Set procedure name
basicManeuver3HornetWing.Name = 'Marshall - Step Down - 2 Kft'

## Set the horizontal/navigation strategy
basicManeuver3HornetWing.NavigationStrategyType = 'Stationkeeping'

# Get the navigation interface
stationkeeping2NavHornetWing = basicManeuver3HornetWing.Navigation

# Set stationkeeping target
stationkeeping2NavHornetWing.TargetName = 'Ship/CVN-72'

# Set station options
stationkeeping2NavHornetWing.RelBearing = -90 # deg
stationkeeping2NavHornetWing.RelRange = 2.7 # nm
stationkeeping2NavHornetWing.DesiredRadius = 2.5 # nm
stationkeeping2NavHornetWing.TurnDirection = TURN_DIRECTION.TURN_LEFT

# Set stop condition options
stationkeeping2NavHornetWing.StopCondition = STATIONKEEPING_STOP_CONDITION.STOP_AFTER_TURN_COUNT
stationkeeping2NavHornetWing.StopAfterTurnCount = 1
stationkeeping2NavHornetWing.UseRelativeCourse = True
stationkeeping2NavHornetWing.StopCourse = -180 # deg

## Set the vertical/profile strategy
basicManeuver3HornetWing.ProfileStrategyType = 'Autopilot - Vertical Plane'

# Get the profile interface
autoProfile2HornetWing = basicManeuver3HornetWing.Profile

# Set the altitude options
autoProfile2HornetWing.AltitudeMode = 1
autoProfile2HornetWing.AbsoluteAltitude = 2000 # ft
autoProfile2HornetWing.AltitudeControlMode = AUTOPILOT_ALTITUDE_CONTROL_MODE.AUTOPILOT_ALTITUDE_RATE
autoProfile2HornetWing.ControlAltitudeRateValue = 2000 # ft/min
autoProfile2HornetWing.ControlLimitMode = PERF_MODEL_OVERRIDE.OVERRIDE
autoProfile2HornetWing.MaxPitchRate = 10 # deg/s
autoProfile2HornetWing.DampingRatio = 2

# Set the airspeed options
autoProfile2HornetWing.AirspeedOptions.AirspeedMode = BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_MAX_ENDURANCE_AIRSPEED
autoProfile2HornetWing.AirspeedOptions.MinSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED
autoProfile2HornetWing.AirspeedOptions.MaxSpeedLimits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED

## Set the attitude/performance/fuel options
basicManeuver3HornetWing.FlightMode = PHASE_OF_FLIGHT.FLIGHT_PHASE_CRUISE
basicManeuver3HornetWing.FuelFlowType = BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_CRUISE

## Set the basic stop conditions
basicManeuver3HornetWing.UseStopFuelState = True
basicManeuver3HornetWing.StopFuelState = 0 # lb
basicManeuver3HornetWing.UseMaxTimeOfFlight = False
basicManeuver3HornetWing.UseMaxDownrange = True
basicManeuver3HornetWing.MaxDownrange = 500 # nm

basicManeuver3HornetWing.AltitudeLimitMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_ERROR
basicManeuver3HornetWing.TerrainImpactMode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_CONTINUE

# Propagate aircraft
avtrPropHornetWing.Propagate()

### End of Script
print('...Scenario done!')