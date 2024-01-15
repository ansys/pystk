"""Demonstrates how to set up a typical STK scenario using STK Engine."""

import os
import tkinter as tk

from ansys.stk.core.stkengine import STKEngine
from ansys.stk.core.stkengine.tkcontrols import GlobeControl, MapControl
from ansys.stk.core.stkobjects import (
    ACCESS_CONSTRAINTS,
    AREA_TYPE,
    AZ_EL_ABOUT_BORESIGHT,
    CLASSICAL_LOCATION,
    CLASSICAL_SIZE_SHAPE,
    DISPLAY_TIMES_TYPE,
    LINE_WIDTH,
    ORIENTATION_ASC_NODE,
    ORIENTATION_TYPE,
    SENSOR_PATTERN,
    SENSOR_POINTING,
    SENSOR_PROJECTION_DISTANCE_TYPE,
    SENSOR_POINTING_TARGETED_BORESIGHT_TYPE,
    STK_OBJECT_TYPE,
    VEHICLE_ATTITUDE,
    VEHICLE_GRAPHICS_2D_ATTRIBUTES,
    VEHICLE_GRAPHICS_2D_VISIBLE_SIDES,
    VEHICLE_PROFILE,
    VEHICLE_PROPAGATOR_TYPE,
    VEHICLE_WAYPOINT_COMP_METHOD,
)
from ansys.stk.core.stkutil import (
    COORDINATE_SYSTEM,
    LINE_STYLE,
    ORBIT_STATE_TYPE,
    POSITION_TYPE,
)
from ansys.stk.core.utilities.colors import Color, Colors


class STKTutorial:
    """Demonstrates how to set up a typical STK scenario using STK Engine."""

    def __init__(self):
        """Create a new instance and initialize the user interface."""
        self.stk = STKEngine.start_application(noGraphics=False)
        self.root = self.stk.new_object_root()
        self.window = tk.Tk()
        self.window.title("STK Tutorial")
        self.window.protocol("WM_DELETE_WINDOW", self._exit)
        self.controlFrame = tk.Frame()
        self.mapControl = MapControl(self.controlFrame, width=640, height=360)
        self.mapControl.back_color = Color.FromRGB(217, 217, 217)
        self.mapControl.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)
        self.globeControl = GlobeControl(
            self.controlFrame, width=640, height=360
        )
        self.globeControl.back_color = Color.FromRGB(217, 217, 217)
        self.globeControl.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)
        self.controlFrame.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT)
        self.buttonFrame = tk.Frame()
        self.newScenarioBtn = tk.Button(
            self.buttonFrame,
            text="New Scenario",
            width=15,
            command=self._new_scenario,
        )
        self.newScenarioBtn.pack(side=tk.TOP, pady=6)
        self.createFacilitiesBtn = tk.Button(
            self.buttonFrame,
            text="Create Facilities",
            width=15,
            wraplength=100,
            command=self._create_facilities,
        )
        self.createFacilitiesBtn.pack(side=tk.TOP, pady=6)
        self.createFacilitiesBtn["state"] = "disabled"
        self.changeFacColorBtn = tk.Button(
            self.buttonFrame,
            text="Change Facilities Color",
            width=15,
            wraplength=100,
            command=self._change_facility_color,
        )
        self.changeFacColorBtn.pack(side=tk.TOP, pady=6)
        self.changeFacColorBtn["state"] = "disabled"
        self.createTargetBtn = tk.Button(
            self.buttonFrame,
            text="Create Target",
            width=15,
            wraplength=100,
            command=self._create_target,
        )
        self.createTargetBtn.pack(side=tk.TOP, pady=6)
        self.createTargetBtn["state"] = "disabled"
        self.createShipBtn = tk.Button(
            self.buttonFrame,
            text="Create Ship",
            width=15,
            wraplength=100,
            command=self._create_ship,
        )
        self.createShipBtn.pack(side=tk.TOP, pady=6)
        self.createShipBtn["state"] = "disabled"
        self.createSatellitesBtn = tk.Button(
            self.buttonFrame,
            text="Create Satellites",
            width=15,
            wraplength=100,
            command=self._create_satellites,
        )
        self.createSatellitesBtn.pack(side=tk.TOP, pady=6)
        self.createSatellitesBtn["state"] = "disabled"
        self.shuttleContoursBtn = tk.Button(
            self.buttonFrame,
            text="Modify Shuttle Contours",
            width=15,
            wraplength=100,
            command=self._configure_shuttle_contours,
        )
        self.shuttleContoursBtn.pack(side=tk.TOP, pady=6)
        self.shuttleContoursBtn["state"] = "disabled"
        self.createAreaTargetsBtn = tk.Button(
            self.buttonFrame,
            text="Create Area Targets",
            width=15,
            command=self._create_area_targets,
        )
        self.createAreaTargetsBtn.pack(side=tk.TOP, pady=6)
        self.createAreaTargetsBtn["state"] = "disabled"
        self.accessBtn = tk.Button(
            self.buttonFrame,
            text="Access",
            width=15,
            command=self._compute_access,
        )
        self.accessBtn.pack(side=tk.TOP, pady=6)
        self.accessBtn["state"] = "disabled"
        self.removeAccessBtn = tk.Button(
            self.buttonFrame,
            text="Remove Access",
            width=15,
            command=self._remove_access,
        )
        self.removeAccessBtn.pack(side=tk.TOP, pady=6)
        self.removeAccessBtn["state"] = "disabled"
        self.createSensorsBtn = tk.Button(
            self.buttonFrame,
            text="Create Sensors",
            width=15,
            command=self._create_sensors,
        )
        self.createSensorsBtn.pack(side=tk.TOP, pady=6)
        self.createSensorsBtn["state"] = "disabled"
        self.sensorVisibilityBtn = tk.Button(
            self.buttonFrame,
            text="Limit Sensor Visibility",
            width=15,
            wraplength=100,
            command=self._configure_sensor_visibility,
        )
        self.sensorVisibilityBtn.pack(side=tk.TOP, pady=6)
        self.sensorVisibilityBtn["state"] = "disabled"
        self.displayIntervalsBtn = tk.Button(
            self.buttonFrame,
            text="Custom Display Intervals",
            width=15,
            wraplength=100,
            command=self._configure_display_intervals,
        )
        self.displayIntervalsBtn.pack(side=tk.TOP, pady=6)
        self.displayIntervalsBtn["state"] = "disabled"
        self.accessIntervalsBtn = tk.Button(
            self.buttonFrame,
            text="Access Display Intervals",
            width=15,
            wraplength=100,
            command=self._configure_access_intervals,
        )
        self.accessIntervalsBtn.pack(side=tk.TOP, pady=6)
        self.accessIntervalsBtn["state"] = "disabled"
        self.rangeConstraintBtn = tk.Button(
            self.buttonFrame,
            text="Range Constraints",
            width=15,
            command=self._configure_range_constraints,
        )
        self.rangeConstraintBtn.pack(side=tk.TOP, pady=6)
        self.rangeConstraintBtn["state"] = "disabled"
        self.buttonFrame.pack(
            fill=tk.BOTH, expand=tk.YES, side=tk.LEFT, padx=10
        )

    def run(self):
        """Run the application."""
        self.window.mainloop()

    def _exit(self):
        self.root.close_scenario()
        self.window.destroy()
        self.stk.shutdown()

    def _new_scenario(self):
        self.root.new_scenario("Tutorial")

        self._configure_units()
        self._configure_time_period()

        self.newScenarioBtn["state"] = "disabled"
        self.createFacilitiesBtn["state"] = "normal"

    def _configure_time_period(self):
        scenario = self.root.current_scenario

        scenario.SetTimePeriod(
            "1 Jul 2023 00:00:00.00", "1 Jul 2023 04:00:00.00"
        )
        scenario.Epoch = "1 Jul 2023 00:00:00.00"

    def _configure_units(self):
        dimensions = self.root.unit_preferences
        dimensions.reset_units()
        dimensions.set_current_unit("DateFormat", "UTCG")
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

    def _create_facilities(self):
        self.baikonur = self.root.current_scenario.children.new(
            STK_OBJECT_TYPE.FACILITY, "Baikonur"
        )
        self.baikonur.UseTerrain = False
        self.planetodetic = self.baikonur.Position.ConvertTo(
            POSITION_TYPE.PLANETODETIC
        )
        self.planetodetic.Lat = 48.0
        self.planetodetic.Lon = 55.0
        self.planetodetic.Alt = 0.0
        self.baikonur.Position.Assign(self.planetodetic)
        self.baikonur.short_description = "Launch Site"
        self.baikonur.long_description = (
            "Launch site in Kazakhstan. Also known as Tyuratam."
        )

        self.perth = self.root.current_scenario.children.new(
            STK_OBJECT_TYPE.FACILITY, "Perth"
        )
        self.perth.UseTerrain = False
        self.planetodetic = self.perth.Position.ConvertTo(
            POSITION_TYPE.PLANETODETIC
        )
        self.planetodetic.Lat = -31.0
        self.planetodetic.Lon = 116.0
        self.planetodetic.Alt = 0
        self.perth.Position.Assign(self.planetodetic)
        self.perth.short_description = "Australian Tracking Station"

        self.wallops = self.root.current_scenario.children.new(
            STK_OBJECT_TYPE.FACILITY, "Wallops"
        )
        self.wallops.UseTerrain = False
        self.planetodetic = self.wallops.Position.ConvertTo(
            POSITION_TYPE.PLANETODETIC
        )
        self.planetodetic.Lat = 37.8602
        self.planetodetic.Lon = -75.5095
        self.planetodetic.Alt = -0.0127878
        self.wallops.Position.Assign(self.planetodetic)
        self.wallops.short_description = "NASA Launch Site/Tracking Station"

        result = self.root.execute_command("GetDirectory / Database Facility")
        facDataDir = result[0]
        filelocation = os.path.join(facDataDir, "stkFacility.fd")
        command = (
            'ImportFromDB * Facility "'
            + filelocation
            + '" Class Facility SiteName "Santiago Station AGO 3 STDN AGO3" '
            + 'Network "NASA NEN" Rename Santiago'
        )
        self.root.execute_command(command)
        command = (
            'ImportFromDB * Facility "'
            + filelocation
            + '" Class Facility SiteName "White Sands" '
            + 'Network "Other" Rename WhiteSands'
        )
        self.root.execute_command(command)

        self.santiago = self.root.current_scenario.children["Santiago"]
        self.whitesands = self.root.current_scenario.children["WhiteSands"]
        self.createFacilitiesBtn["state"] = "disabled"
        self.changeFacColorBtn["state"] = "normal"

    def _change_facility_color(self):
        self.baikonur.Graphics.Color = Colors.Black
        self.perth.Graphics.Color = Colors.White
        self.wallops.Graphics.Color = Colors.Gray
        self.santiago.Graphics.Color = Colors.DarkGreen
        self.whitesands.Graphics.Color = Colors.LightSeaGreen
        self.changeFacColorBtn["state"] = "disabled"
        self.createTargetBtn["state"] = "normal"

    def _create_target(self):
        self.iceberg = self.root.current_scenario.children.new(
            STK_OBJECT_TYPE.TARGET, "Iceberg"
        )
        self.iceberg.UseTerrain = False
        self.planetodetic = self.iceberg.Position.ConvertTo(
            POSITION_TYPE.PLANETODETIC
        )
        self.planetodetic.Lat = 74.91
        self.planetodetic.Lon = -74.5
        self.planetodetic.Alt = 0.0

        self.iceberg.Position.Assign(self.planetodetic)
        self.iceberg.short_description = "Only the tip."
        self.createTargetBtn["state"] = "disabled"
        self.createShipBtn["state"] = "normal"

    def _add_waypoint(self, waypoints, Lat, Lon, Alt, Speed, tr):
        elem = waypoints.Add()
        elem.Latitude = Lat
        elem.Longitude = Lon
        elem.Altitude = Alt
        elem.Speed = Speed
        elem.TurnRadius = tr

    def _create_ship(self):
        cruise = self.root.current_scenario.children.new(
            STK_OBJECT_TYPE.SHIP, "Cruise"
        )
        cruise.SetRouteType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        greatArc = cruise.Route
        interval = greatArc.EphemerisInterval
        interval.SetExplicitInterval(
            "1 Jul 2023 00:00:00.00", interval.FindStopTime()
        )
        greatArc.Method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL

        self._add_waypoint(greatArc.Waypoints, 44.1, -8.5, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 51.0, -26.6, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 52.1, -40.1, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 60.2, -55.0, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 68.2, -65.0, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 72.5, -70.1, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 74.9, -74.5, 0.0, 0.015, 0.0)

        cruise.SetAttitudeType(VEHICLE_ATTITUDE.ATTITUDE_STANDARD)
        attitude = cruise.Attitude
        attitude.Basic.SetProfileType(
            VEHICLE_PROFILE.PROFILE_ECF_VELOCITY_ALIGNMENT_WITH_RADIAL_CONSTRAINT
        )
        cruise.Graphics.WaypointMarker.IsWaypointMarkersVisible = True
        cruise.Graphics.WaypointMarker.IsTurnMarkersVisible = True
        greatArc.Propagate()
        self.root.rewind()
        self.createShipBtn["state"] = "disabled"
        self.createSatellitesBtn["state"] = "normal"

    def _create_satellites(self):
        tdrs = self.root.current_scenario.children.new(
            STK_OBJECT_TYPE.SATELLITE, "TDRS"
        )
        tdrs.SetPropagatorType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twobody = tdrs.Propagator

        classical = twobody.InitialState.Representation.ConvertTo(
            ORBIT_STATE_TYPE.CLASSICAL
        )
        classical.CoordinateSystemType = (
            COORDINATE_SYSTEM.J2000
        )
        interval = twobody.EphemerisInterval
        interval.SetExplicitInterval(
            "1 Jul 2023 00:00:00.000", "1 Jul 2023 04:00:00.000"
        )
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

        result = self.root.execute_command("GetDirectory / Database Satellite")
        satDataDir = result[0]
        filelocation = os.path.join(satDataDir, "stkSatDb.sd")
        command = (
            'ImportFromDB * Satellite "'
            + filelocation
            + '" Rename TDRS_3 Propagate On CommonName "TDRS 3"'
        )
        self.root.execute_command(command)

        tdrsC = self.root.current_scenario.children["TDRS_3"]
        sgp4 = tdrsC.Propagator
        interval = sgp4.EphemerisInterval
        interval.SetExplicitInterval(
            "1 Jul 2023 00:00:00.000", "1 Jul 2023 04:00:00.000"
        )

        self.ers1 = self.root.current_scenario.children.new(
            STK_OBJECT_TYPE.SATELLITE, "ERS1"
        )
        self.ers1.SetPropagatorType(
            VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION
        )
        j4 = self.ers1.Propagator
        interval = j4.EphemerisInterval
        interval.SetExplicitInterval(
            "1 Jul 2023 00:00:00.000", "1 Jul 2023 04:00:00.000"
        )
        j4.Step = 60.00
        oOrb = j4.InitialState.Representation
        oOrb.Epoch = "1 Jul 2023 00:00:00.000"

        classical = j4.InitialState.Representation.ConvertTo(
            ORBIT_STATE_TYPE.CLASSICAL
        )
        classical.CoordinateSystemType = (
            COORDINATE_SYSTEM.J2000
        )
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
        self.root.rewind()
        self.ers1.Graphics.Passes.VisibleSides = (
            VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_DESCENDING
        )
        self.ers1.Graphics.Passes.VisibleSides = (
            VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_BOTH
        )
        self.shuttle = self.root.current_scenario.children.new(
            STK_OBJECT_TYPE.SATELLITE, "Shuttle"
        )
        self.shuttle.SetPropagatorType(
            VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION
        )
        j4 = self.shuttle.Propagator
        interval = j4.EphemerisInterval
        interval.SetExplicitInterval(
            "1 Jul 2023 00:00:00.000", "1 Jul 2023 03:00:00.000"
        )
        j4.Step = 60.00
        oOrb = j4.InitialState.Representation
        oOrb.Epoch = "1 Jul 2023 00:00:00.000"

        classical = j4.InitialState.Representation.ConvertTo(
            ORBIT_STATE_TYPE.CLASSICAL
        )
        classical.CoordinateSystemType = (
            COORDINATE_SYSTEM.J2000
        )
        classical.LocationType = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
        trueAnomaly = classical.Location
        trueAnomaly.Value = 0.0
        classical.SizeShapeType = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_ALTITUDE
        altitude = classical.SizeShape
        altitude.ApogeeAltitude = 370.4
        altitude.PerigeeAltitude = 370.4
        classical.Orientation.ArgOfPerigee = 0.0
        classical.Orientation.AscNodeType = ORIENTATION_ASC_NODE.ASC_NODE_LAN
        lan = classical.Orientation.AscNode
        lan.Value = -151.0
        classical.Orientation.Inclination = 28.5
        j4.InitialState.Representation.Assign(classical)

        j4.Propagate()
        self.root.rewind()
        self.createSatellitesBtn["state"] = "disabled"
        self.shuttleContoursBtn["state"] = "normal"

    def _configure_shuttle_contours(self):
        self.shuttle.Graphics.SetAttributesType(
            VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC
        )
        orbitgfx = self.shuttle.Graphics.Attributes
        orbitgfx.Line.Style = LINE_STYLE.DASHED
        orbitgfx.MarkerStyle = "Plus"

        contours = self.shuttle.Graphics.ElevContours
        elevations = contours.Elevations
        elevations.RemoveAll()
        elevations.AddLevelRange(0, 50, 10)

        for elem in elevations:
            elem.DistanceVisible = False
            elem.LineStyle = LINE_STYLE.DOT_DASHED
            elem.LineWidth = LINE_WIDTH.WIDTH3

        contours.IsVisible = True
        self.root.rewind()
        self.shuttleContoursBtn["state"] = "disabled"
        self.createAreaTargetsBtn["state"] = "normal"

    def _create_area_targets(self):
        self.searchArea = self.root.current_scenario.children.new(
            STK_OBJECT_TYPE.AREA_TARGET, "SearchArea"
        )
        atGfx = self.searchArea.Graphics
        atGfx.MarkerStyle = "None"
        atGfx.Inherit = False
        atGfx.LabelVisible = False
        atGfx.CentroidVisible = False

        self.searchArea.AutoCentroid = False
        self.searchArea.AreaType = AREA_TYPE.PATTERN
        patterns = self.searchArea.AreaTypeData
        patterns.Add(78.4399, -77.6125)
        patterns.Add(77.7879, -71.1578)
        patterns.Add(74.5279, -69.0714)
        patterns.Add(71.6591, -69.1316)
        patterns.Add(70.0291, -70.8318)
        patterns.Add(71.9851, -76.3086)

        self.searchArea.UseTerrainData = False
        sphere = self.searchArea.Position.ConvertTo(POSITION_TYPE.SPHERICAL)
        sphere.Lat = 74.9533
        sphere.Lon = -74.5482
        sphere.Radius = 6358.186790
        self.searchArea.Position.Assign(sphere)
        self.createAreaTargetsBtn["state"] = "disabled"
        self.accessBtn["state"] = "normal"

    def _compute_access(self):
        self.access = self.ers1.get_access_to_object(self.searchArea)
        self.access.compute_access()
        self.root.rewind()

        interval = self.access.data_providers["Access Data"]
        result = interval.Exec(
            "1 Jul 2023 00:00:00.000", "1 Jul 2023 04:00:00.000"
        )
        print("Access intervals:")
        for interval in result.Intervals:
            print(f"{interval.StartTime} {interval.StopTime}")

        self.accessBtn["state"] = "disabled"
        self.removeAccessBtn["state"] = "normal"

    def _remove_access(self):
        self.access.remove_access()
        self.root.rewind()
        self.removeAccessBtn["state"] = "disabled"
        self.createSensorsBtn["state"] = "normal"

    def _create_sensors(self):
        self.horizon = self.root.current_scenario.children["ERS1"].children.new(
            STK_OBJECT_TYPE.SENSOR, "Horizon"
        )
        self.horizon.SetPatternType(SENSOR_PATTERN.SIMPLE_CONIC)
        simpleConic = self.horizon.Pattern
        simpleConic.ConeAngle = 90
        self.horizon.SetPointingType(SENSOR_POINTING.POINT_FIXED)
        fixedPt = self.horizon.Pointing
        azEl = fixedPt.Orientation.ConvertTo(ORIENTATION_TYPE.AZ_EL)
        azEl.Elevation = 90
        azEl.AboutBoresight = AZ_EL_ABOUT_BORESIGHT.ROTATE
        fixedPt.Orientation.Assign(azEl)

        # removing the ers1 elevcontours from the 2d window
        self.ers1.Graphics.ElevContours.IsVisible = False
        downlink = self.root.current_scenario.children["ERS1"].children.new(
            STK_OBJECT_TYPE.SENSOR, "Downlink"
        )
        downlink.SetPatternType(SENSOR_PATTERN.HALF_POWER)
        halfpower = downlink.Pattern
        halfpower.Frequency = 0.85
        halfpower.AntennaDiameter = 1.0

        downlink.SetPointingType(SENSOR_POINTING.POINT_TARGETED)
        targeted = downlink.Pointing
        targeted.Boresight = SENSOR_POINTING_TARGETED_BORESIGHT_TYPE.TRACKING
        targets = targeted.Targets
        targets.Add("Facility/Baikonur")
        targets.Add("Facility/WhiteSands")
        targets.Add("Facility/Perth")
        targets.AddObject(self.santiago)
        targets.Add(self.wallops.path)

        self.root.rewind()
        self.createSensorsBtn["state"] = "disabled"
        self.sensorVisibilityBtn["state"] = "normal"

    def _configure_sensor_visibility(self):
        fiveDegElev = self.root.current_scenario.children[
            "Wallops"
        ].children.new(STK_OBJECT_TYPE.SENSOR, "FiveDegElev")

        fiveDegElev.SetPatternType(SENSOR_PATTERN.COMPLEX_CONIC)
        complexConic = fiveDegElev.Pattern
        complexConic.InnerConeHalfAngle = 0
        complexConic.OuterConeHalfAngle = 85
        complexConic.MinimumClockAngle = 0
        complexConic.MaximumClockAngle = 360

        fiveDegElev.SetPointingType(SENSOR_POINTING.POINT_FIXED)
        fixedPt = fiveDegElev.Pointing
        azEl = fixedPt.Orientation.ConvertTo(ORIENTATION_TYPE.AZ_EL)
        azEl.Elevation = 90
        azEl.AboutBoresight = AZ_EL_ABOUT_BORESIGHT.ROTATE
        fixedPt.Orientation.Assign(azEl)

        fiveDegElev.Graphics.Projection.DistanceType = (
            SENSOR_PROJECTION_DISTANCE_TYPE.CONSTANT_ALTITUDE
        )
        dispDistance = fiveDegElev.Graphics.Projection.DistanceData
        dispDistance.Max = 785.248
        dispDistance.Min = 0
        dispDistance.NumberOfSteps = 1
        self.root.rewind()
        self.sensorVisibilityBtn["state"] = "disabled"
        self.displayIntervalsBtn["state"] = "normal"

    def _configure_display_intervals(self):
        j4 = self.ers1.Propagator
        interval = j4.EphemerisInterval
        interval.SetExplicitInterval(
            interval.FindStartTime(), "2 Jul 2023 00:00:00.000"
        )
        j4.Propagate()

        self.ers1.Graphics.SetAttributesType(
            VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_CUSTOM
        )
        customAtt = self.ers1.Graphics.Attributes
        gfxInterval = customAtt.Intervals.Add(
            "1 Jul 2023 11:30:00.000", "1 Jul 2023 12:00:00.000"
        )
        gfxInterval.GfxAttributes.Color = Colors.FromRGB(156, 49, 24)
        gfxInterval.GfxAttributes.IsVisible = True
        gfxInterval.GfxAttributes.Inherit = True

        gfxInterval = customAtt.Intervals.Add(
            "1 Jul 2023 23:30:00.000", "1 Jul 2023 24:00:00.000"
        )
        gfxInterval.GfxAttributes.Color = Colors.FromRGB(116, 80, 94)
        gfxInterval.GfxAttributes.IsVisible = True
        gfxInterval.GfxAttributes.Inherit = True
        self.root.rewind()
        self.displayIntervalsBtn["state"] = "disabled"
        self.accessIntervalsBtn["state"] = "normal"

    def _configure_access_intervals(self):
        self.ers1.Graphics.SetAttributesType(
            VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_ACCESS
        )
        gfxAccess = self.ers1.Graphics.Attributes

        gfxAccess.AccessObjects.Add("Facility/Wallops")
        gfxAccess.AccessObjects.Add("Facility/Santiago")
        gfxAccess.AccessObjects.Add("Facility/Baikonur")
        gfxAccess.AccessObjects.Add("Facility/Perth")
        gfxAccess.AccessObjects.Add(self.whitesands.path)

        orbitGfx = gfxAccess.NoAccess
        orbitGfx.IsVisible = True
        orbitGfx.Inherit = False
        orbitGfx.IsGroundMarkerVisible = False
        orbitGfx.IsOrbitMarkerVisible = False

        horizonDispTm = self.horizon
        horizonDispTm.SetDisplayStatusType(DISPLAY_TIMES_TYPE.DURING_ACCESS)
        duringAccess = horizonDispTm.DisplayTimesData

        accessObjects = duringAccess.AccessObjects
        accessObjects.Add("Facility/Wallops")
        accessObjects.Add("Facility/Santiago")
        accessObjects.Add("Facility/Baikonur")
        accessObjects.AddObject(self.perth)
        accessObjects.Add(self.whitesands.path)
        self.root.rewind()
        self.accessIntervalsBtn["state"] = "disabled"
        self.rangeConstraintBtn["state"] = "normal"

    def _configure_range_constraints(self):
        access = self.horizon.get_access_to_object(self.baikonur)
        access.compute_access()
        minMax = self.horizon.access_constraints.add_constraint(
            ACCESS_CONSTRAINTS.RANGE
        )

        minMax.EnableMax = True
        minMax.Max = 2000
        minMax.Max = 1500
        minMax.Max = 1000
        minMax.Max = 500
        self.root.rewind()
        self.rangeConstraintBtn["state"] = "disabled"


if __name__ == "__main__":
    stk_tutorial = STKTutorial()
    stk_tutorial.run()
