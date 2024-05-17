import os

try:
    if os.name == "nt":
        from ansys.stk.core.stkdesktop import STKDesktop
    from ansys.stk.core.stkobjects import *
    from ansys.stk.core.stkutil import *
    from ansys.stk.core.utilities.colors import *
except:
    print("Failed to import stk modules. Make sure you have installed the STK Python API wheel (agi.stk<..ver..>-py3-none-any.whl) from the STK Install bin directory")

def AddWaypoint(waypoints, Lat, Lon, Alt, Speed, tr):
    elem = waypoints.Add()
    elem.Latitude = Lat
    elem.Longitude = Lon
    elem.Altitude = Alt
    elem.Speed = Speed
    elem.TurnRadius = tr
    
def main():
    if os.name == "nt":
        app = STKDesktop.start_application(visible=True, userControl=True)
        ObjectRoot = app.root
    else:
        print("Automation samples only work on windows with the desktop application, see Custom Applications for STK Engine examples.")
        quit()

    #part1
    print("New Scenario...")
    ObjectRoot.new_scenario("ProTutorial")

    dimensions = ObjectRoot.unit_preferences
    dimensions.reset_units()
    dimensions.set_current_unit("DateFormat", "UTCG")
    scene = ObjectRoot.current_scenario

    scene.StartTime = "1 Jul 2002 00:00:00.00"
    scene.StopTime = "1 Jul 2002 04:00:00.00"
    scene.Epoch = "1 Jul 2002 00:00:00.00"

    dimensions.set_current_unit("DistanceUnit", "km")
    dimensions.set_current_unit("TimeUnit", "sec")
    dimensions.set_current_unit("AngleUnit", "deg")
    dimensions.set_current_unit("MassUnit", "kg")
    dimensions.set_current_unit("PowerUnit", "dbw")
    dimensions.set_current_unit("FrequencyUnit", "ghz")
    dimensions.set_current_unit("SmallDistanceUnit", "m")
    dimensions.set_current_unit("latitudeUnit", "deg")
    dimensions.set_current_unit("longitudeunit", "deg")
    dimensions.set_current_unit("DurationUnit", "HMS")
    dimensions.set_current_unit("Temperature", "K")
    dimensions.set_current_unit("SmallTimeUnit", "sec")
    dimensions.set_current_unit("RatioUnit", "db")
    dimensions.set_current_unit("rcsUnit", "dbsm")
    dimensions.set_current_unit("DopplerVelocityUnit", "m/s")
    dimensions.set_current_unit("Percent", "unitValue")
    input("Press enter to continue...")

    #part2
    print("Create Facilities...")
    baikonur = ObjectRoot.current_scenario.children.new(STK_OBJECT_TYPE.eFacility, "Baikonur")
    baikonur.UseTerrain = False
    planetodetic = baikonur.Position.ConvertTo(POSITION_TYPE.PLANETODETIC)
    planetodetic.Lat = 48.0
    planetodetic.Lon = 55.0
    planetodetic.Alt = 0.0
    baikonur.Position.Assign(planetodetic)
    baikonur.short_description = "Launch Site"
    baikonur.long_description = "Launch site in Kazakhstan. Also known as Tyuratam."

    perth = ObjectRoot.current_scenario.children.new(STK_OBJECT_TYPE.eFacility, "Perth")
    perth.UseTerrain = False
    planetodetic = perth.Position.ConvertTo(POSITION_TYPE.PLANETODETIC)
    planetodetic.Lat = -31.0
    planetodetic.Lon = 116.0
    planetodetic.Alt = 0
    perth.Position.Assign(planetodetic)
    perth.short_description = "Australian Tracking Station"

    wallops = ObjectRoot.current_scenario.children.new(STK_OBJECT_TYPE.eFacility, "Wallops")
    wallops.UseTerrain = False
    planetodetic = wallops.Position.ConvertTo(POSITION_TYPE.PLANETODETIC)
    planetodetic.Lat = 37.8602
    planetodetic.Lon = -75.5095
    planetodetic.Alt = -0.0127878
    wallops.Position.Assign(planetodetic)
    wallops.short_description = "NASA Launch Site/Tracking Station"

    result = ObjectRoot.execute_command("GetDirectory / Database Facility")
    facDataDir = result[0]
    filelocation = facDataDir + os.path.sep + "stkFacility.fd"
    command = "ImportFromDB * Facility \"" + filelocation + "\"Class Facility SiteName \"Santiago Station AGO 3 STDN AGO3\" Network \"NASA NEN\" Rename Santiago"
    ObjectRoot.execute_command(command)
    command = "ImportFromDB * Facility \"" + filelocation + "\"Class Facility SiteName \"White Sands\" Network \"Other\" Rename WhiteSands"
    ObjectRoot.execute_command(command)

    santiago = ObjectRoot.current_scenario.children["Santiago"]
    whitesands = ObjectRoot.current_scenario.children["WhiteSands"]
    input("Press enter to continue...")

    #part3
    print("Change Facilities Color...")
    baikonur.Graphics.Color = Colors.FromRGB(0, 0, 0)
    perth.Graphics.Color = Colors.FromRGB(167, 77, 215)
    wallops.Graphics.Color = Colors.FromRGB(134, 217, 72)
    santiago.Graphics.Color = Colors.FromRGB(88,88,8)
    whitesands.Graphics.Color = Colors.FromRGB(123, 45, 67)
    input("Press enter to continue...")

    #part4
    print("Create Target...")
    iceberg = ObjectRoot.current_scenario.children.new(STK_OBJECT_TYPE.eTarget, "Iceberg")
    iceberg.UseTerrain = False
    planetodetic = iceberg.Position.ConvertTo(POSITION_TYPE.PLANETODETIC)
    planetodetic.Lat = 74.91
    planetodetic.Lon = -74.5
    planetodetic.Alt = 0.0

    iceberg.Position.Assign(planetodetic)
    iceberg.short_description = "Only the tip."
    input("Press enter to continue...")

    #part5
    print("Create Ship...")
    cruise = ObjectRoot.current_scenario.children.new(STK_OBJECT_TYPE.eShip, "Cruise")
    cruise.SetRouteType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
    greatArc = cruise.Route
    interval = greatArc.EphemerisInterval
    interval.SetExplicitInterval("1 Jul 2002 00:00:00.00", interval.FindStopTime())
    greatArc.Method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL

    AddWaypoint(greatArc.Waypoints, 44.1, -8.5, 0.0, .015, 0.0)
    AddWaypoint(greatArc.Waypoints, 51.0, -26.6, 0.0, .015, 0.0)
    AddWaypoint(greatArc.Waypoints, 52.1, -40.1, 0.0, .015, 0.0)
    AddWaypoint(greatArc.Waypoints, 60.2, -55.0, 0.0, .015, 0.0)
    AddWaypoint(greatArc.Waypoints, 68.2, -65.0, 0.0, .015, 0.0)
    AddWaypoint(greatArc.Waypoints, 72.5, -70.1, 0.0, .015, 0.0)
    AddWaypoint(greatArc.Waypoints, 74.9, -74.5, 0.0, .015, 0.0)

    cruise.SetAttitudeType(VEHICLE_ATTITUDE.ATTITUDE_STANDARD)
    attitude = cruise.Attitude
    attitude.Basic.SetProfileType(VEHICLE_PROFILE.PROFILE_ECF_VELOCITY_ALIGNMENT_WITH_RADIAL_CONSTRAINT)
    cruise.Graphics.WaypointMarker.IsWaypointMarkersVisible = True
    cruise.Graphics.WaypointMarker.IsTurnMarkersVisible = True
    greatArc.Propagate()
    ObjectRoot.rewind()
    input("Press enter to continue...")
    
    #part6
    print("Create Satellites...")
    tdrs = ObjectRoot.current_scenario.children.new(STK_OBJECT_TYPE.eSatellite, "TDRS")
    tdrs.SetPropagatorType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
    twobody = tdrs.Propagator

    classical = twobody.InitialState.Representation.ConvertTo(ORBIT_STATE_TYPE.CLASSICAL)
    classical.CoordinateSystemType = COORDINATE_SYSTEM.J2000
    interval = twobody.EphemerisInterval
    interval.SetExplicitInterval("1 Jul 2002 00:00:00.000", "1 Jul 2002 04:00:00.000")
    twobody.Step = 60
    classical.LocationType = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
    trueAnomaly = classical.Location
    trueAnomaly.Value = 178.845262

    classical.SizeShapeType = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_PERIOD
    period = classical.SizeShape
    period.Eccentricity = 0.0
    period.Period = 86164.090540
    classical.Orientation.ArgOfPerigee = 0.0
    classical.Orientation.Inclination = 0.0
    classical.Orientation.AscNodeType = ORIENTATION_ASC_NODE.ASC_NODE_LAN
    lan = classical.Orientation.AscNode
    lan.Value = 259.999982

    twobody.InitialState.Representation.Assign(classical)
    twobody.Propagate()

    result = ObjectRoot.execute_command("GetDirectory / Database Satellite")
    satDataDir = result[0]
    filelocation = satDataDir + os.path.sep + "stkSatDb.sd"
    command = "ImportFromDB * Satellite \"" + filelocation + "\" Rename TDRS_3 Propagate On CommonName \"TDRS 3\""
    ObjectRoot.execute_command(command)

    tdrsC = ObjectRoot.current_scenario.children["TDRS_3"]
    sgp4 = tdrsC.Propagator
    interval = sgp4.EphemerisInterval
    interval.SetExplicitInterval("1 Jul 2002 00:00:00.000", "1 Jul 2002 04:00:00.000")

    ers1 = ObjectRoot.current_scenario.children.new(STK_OBJECT_TYPE.eSatellite, "ERS1")
    ers1.SetPropagatorType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
    j4 = ers1.Propagator
    interval = j4.EphemerisInterval
    interval.SetExplicitInterval("1 Jul 2002 00:00:00.000", "1 Jul 2002 04:00:00.000")
    j4.Step = 60.00
    oOrb = j4.InitialState.Representation
    oOrb.Epoch = "1 Jul 2002 00:00:00.000"

    classical = j4.InitialState.Representation.ConvertTo(ORBIT_STATE_TYPE.CLASSICAL)
    classical.CoordinateSystemType = COORDINATE_SYSTEM.J2000
    classical.LocationType = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
    trueAnomaly = classical.Location
    trueAnomaly.Value = 0.0
    classical.SizeShapeType = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_SEMIMAJOR_AXIS
    semi = classical.SizeShape
    semi.SemiMajorAxis = 7163.14
    semi.Eccentricity = 0.0
    classical.Orientation.ArgOfPerigee = 0.0
    classical.Orientation.AscNodeType = ORIENTATION_ASC_NODE.ASC_NODE_LAN
    lan = classical.Orientation.AscNode
    lan.Value = 99.38
    classical.Orientation.Inclination = 98.50
    j4.InitialState.Representation.Assign(classical)
    j4.Propagate()

    ObjectRoot.rewind()
    ers1.Graphics.Passes.VisibleSides = VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_DESCENDING
    ers1.Graphics.Passes.VisibleSides = VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_BOTH
    shuttle = ObjectRoot.current_scenario.children.new(STK_OBJECT_TYPE.eSatellite, "Shuttle")
    shuttle.SetPropagatorType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
    j4 = shuttle.Propagator
    interval = j4.EphemerisInterval
    interval.SetExplicitInterval("1 Jul 2002 00:00:00.000", "1 Jul 2002 03:00:00.000")
    j4.Step = 60.00

    oOrb = j4.InitialState.Representation
    oOrb.Epoch = "1 Jul 2002 00:00:00.000"

    classical = j4.InitialState.Representation.ConvertTo(ORBIT_STATE_TYPE.CLASSICAL)
    classical.CoordinateSystemType = COORDINATE_SYSTEM.J2000
    classical.LocationType = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
    trueAnomaly = classical.Location
    trueAnomaly.Value = 0.0
    classical.SizeShapeType = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_ALTITUDE
    altitude = classical.SizeShape
    altitude.ApogeeAltitude= 370.4
    altitude.PerigeeAltitude = 370.4
    classical.Orientation.ArgOfPerigee = 0.0
    classical.Orientation.AscNodeType = ORIENTATION_ASC_NODE.ASC_NODE_LAN
    lan = classical.Orientation.AscNode
    lan.Value = -151.0
    classical.Orientation.Inclination = 28.5

    j4.InitialState.Representation.Assign(classical)
    j4.Propagate()
    ObjectRoot.rewind()
    input("Press enter to continue...")
    
    #part7
    print("Modify Shuttle Contours...")
    shuttle.Graphics.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)
    orbitgfx = shuttle.Graphics.Attributes
    orbitgfx.Line.Style = LINE_STYLE.eDashed
    orbitgfx.MarkerStyle = "Plus"

    contours = shuttle.Graphics.ElevContours
    elevations = contours.Elevations
    elevations.RemoveAll()
    elevations.AddLevelRange(0, 50, 10)

    for elem in elevations:
        elem.DistanceVisible = False
        elem.LineStyle = LINE_STYLE.eDotDashed
        elem.LineWidth = LINE_WIDTH.WIDTH3

    contours.IsVisible = True
    ObjectRoot.rewind()
    input("Press enter to continue...")
    
    #part8
    print("Create Area Targets...")
    searchArea = ObjectRoot.current_scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "SearchArea")
    atGfx = searchArea.Graphics
    atGfx.MarkerStyle = "None"
    atGfx.Inherit = False
    atGfx.LabelVisible = False
    atGfx.CentroidVisible = False

    searchArea.AutoCentroid = False

    searchArea.AreaType = AREA_TYPE.PATTERN
    patterns = searchArea.AreaTypeData
    patterns.Add(78.4399, -77.6125)
    patterns.Add(77.7879, -71.1578)
    patterns.Add(74.5279, -69.0714)
    patterns.Add(71.6591, -69.1316)
    patterns.Add(70.0291, -70.8318)
    patterns.Add(71.9851, -76.3086)

    searchArea.UseTerrainData = False
    sphere = searchArea.Position.ConvertTo(POSITION_TYPE.SPHERICAL)
    sphere.Lat = 74.9533
    sphere.Lon = -74.5482
    sphere.Radius = 6358.186790
    searchArea.Position.Assign(sphere)
    input("Press enter to continue...")
    
    #part9
    print("Access...")
    access = ers1.get_access_to_object(searchArea)
    access.compute_access()
    ObjectRoot.rewind()

    interval = access.data_providers["Access Data"]
    result = interval.Exec("1 Jul 2002 00:00:00.000", "1 Jul 2002 04:00:00.000")
    #With the result returned, the user can use the data any way they prefer.
    input("Press enter to continue...")
    
    #part10
    print("Remove Access...")
    access.remove_access()
    ObjectRoot.rewind()
    input("Press enter to continue...")
    
    #part11
    print("Create Sensors...")
    horizon = ObjectRoot.current_scenario.children["ERS1"].children.new(STK_OBJECT_TYPE.eSensor, "Horizon")
    horizon.SetPatternType(SENSOR_PATTERN.SIMPLE_CONIC)
    simpleConic  = horizon.Pattern
    simpleConic.ConeAngle = 90
    horizon.SetPointingType(SENSOR_POINTING.POINT_FIXED)
    fixedPt = horizon.Pointing
    azEl = fixedPt.Orientation.ConvertTo(ORIENTATION_TYPE.AZ_EL)
    azEl.Elevation = 90
    azEl.AboutBoresight = AZ_EL_ABOUT_BORESIGHT.ROTATE
    fixedPt.Orientation.Assign(azEl)

    #removing the ers1 elevcontours from the 2d window
    ers1.Graphics.ElevContours.IsVisible = False
    
    downlink = ObjectRoot.current_scenario.children["ERS1"].children.new(STK_OBJECT_TYPE.eSensor, "Downlink")
    downlink.SetPatternType(SENSOR_PATTERN.HALF_POWER)
    halfpower = downlink.Pattern
    halfpower.Frequency = .85
    halfpower.AntennaDiameter = 1.0
    downlink.SetPointingType(SENSOR_POINTING.POINT_TARGETED)
    targeted = downlink.Pointing
    targeted.Boresight = SENSOR_POINTING_TARGETED_BORESIGHT_TYPE.TRACKING
    targets = targeted.Targets
    targets.Add("Facility/Baikonur")
    targets.Add("Facility/WhiteSands")
    targets.Add("Facility/Perth")
    targets.AddObject(santiago)
    targets.Add(wallops.path)
    ObjectRoot.rewind()
    input("Press enter to continue...")
    
    #part12
    print("Limit Sensor Visibility...")
    fiveDegElev = ObjectRoot.current_scenario.children["Wallops"].children.new(STK_OBJECT_TYPE.eSensor, "FiveDegElev")

    fiveDegElev.SetPatternType(SENSOR_PATTERN.COMPLEX_CONIC)
    complexConic = fiveDegElev.Pattern
    complexConic.InnerConeHalfAngle = 0
    complexConic.OuterConeHalfAngle = 85
    complexConic.MinimumClockAngle = 0
    complexConic.MaximumClockAngle = 360

    fiveDegElev.SetPointingType(SENSOR_POINTING.POINT_FIXED)
    fixedPt = fiveDegElev.Pointing
    azEl = fixedPt.Orientation.ConvertTo(ORIENTATION_TYPE.AZ_EL)
    azEl.Elevation= 90
    azEl.AboutBoresight = AZ_EL_ABOUT_BORESIGHT.ROTATE
    fixedPt.Orientation.Assign(azEl)

    fiveDegElev.Graphics.Projection.DistanceType = SENSOR_PROJECTION_DISTANCE_TYPE.CONSTANT_ALTITUDE
    dispDistance = fiveDegElev.Graphics.Projection.DistanceData
    dispDistance.Max = 785.248
    dispDistance.Min = 0
    dispDistance.NumberOfSteps = 1
    ObjectRoot.rewind()
    input("Press enter to continue...")
    
    #part13
    print("Custom Display Intervals...")
    j4 = ers1.Propagator
    interval = j4.EphemerisInterval
    interval.SetExplicitInterval(interval.FindStartTime(), "2 Jul 2002 00:00:00.000")
    j4.Propagate()

    ers1.Graphics.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_CUSTOM)
    customAtt = ers1.Graphics.Attributes
    gfxInterval = customAtt.Intervals.Add("1 Jul 2002 11:30:00.000", "1 Jul 2002 12:00:00.000")
    gfxInterval.GfxAttributes.Color = Colors.FromRGB(156, 49, 24)
    gfxInterval.GfxAttributes.IsVisible = True
    gfxInterval.GfxAttributes.Inherit= True

    gfxInterval = customAtt.Intervals.Add("1 Jul 2002 23:30:00.000", "1 Jul 2002 24:00:00.000")
    gfxInterval.GfxAttributes.Color = Colors.FromRGB(116, 80, 94)
    gfxInterval.GfxAttributes.IsVisible = True
    gfxInterval.GfxAttributes.Inherit = True
    ObjectRoot.rewind()
    input("Press enter to continue...")
    
    #part14
    print("Access Display Intervals...")
    ers1.Graphics.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_ACCESS)
    gfxAccess = ers1.Graphics.Attributes

    gfxAccess.AccessObjects.Add("Facility/Wallops")
    gfxAccess.AccessObjects.Add("Facility/Santiago")
    gfxAccess.AccessObjects.Add("Facility/Baikonur")
    gfxAccess.AccessObjects.Add("Facility/Perth")
    gfxAccess.AccessObjects.Add(whitesands.path)

    orbitGfx = gfxAccess.NoAccess
    orbitGfx.IsVisible = True
    orbitGfx.Inherit = False
    orbitGfx.IsGroundMarkerVisible = False
    orbitGfx.IsOrbitMarkerVisible = False

    horizonDispTm = horizon
    horizonDispTm.SetDisplayStatusType(DISPLAY_TIMES_TYPE.DURING_ACCESS)
    duringAccess = horizonDispTm.DisplayTimesData

    accessObjects = duringAccess.AccessObjects
    accessObjects.Add("Facility/Wallops")
    accessObjects.Add("Facility/Santiago")
    accessObjects.Add("Facility/Baikonur")
    accessObjects.AddObject(perth)
    accessObjects.Add(whitesands.path)
    ObjectRoot.rewind()
    input("Press enter to continue...")
    
    #part15
    print("Range Constraints...")
    access = horizon.get_access_to_object(baikonur)
    access.compute_access()
    minMax = horizon.access_constraints.add_constraint(ACCESS_CONSTRAINTS.RANGE)

    minMax.EnableMax = True
    minMax.Max = 2000
    minMax.Max = 1500
    minMax.Max = 1000
    minMax.Max = 500
    ObjectRoot.rewind()

    print("Finished...")
    input("Press enter to close the application...")

    #close scenario
    ObjectRoot.close_scenario()
    app.shutdown()
    
if __name__ == '__main__':
    main()