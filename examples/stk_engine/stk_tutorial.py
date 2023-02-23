"""Demonstrates how to set up a typical STK scenario using STK Engine."""

import os
import tkinter as tk

from ansys.stk.core.stkengine import STKEngine
from ansys.stk.core.stkengine.tkcontrols import GlobeControl, MapControl
from ansys.stk.core.stkobjects import (
    AgEAccessConstraints,
    AgEAreaType,
    AgEAzElAboutBoresight,
    AgEClassicalLocation,
    AgEClassicalSizeShape,
    AgEDisplayTimesType,
    AgELineWidth,
    AgEOrientationAscNode,
    AgEOrientationType,
    AgESnPattern,
    AgESnPointing,
    AgESnProjectionDistanceType,
    AgESnPtTrgtBsightType,
    AgESTKObjectType,
    AgEVeAttitude,
    AgEVeGfxAttributes,
    AgEVeGfxVisibleSides,
    AgEVeProfile,
    AgEVePropagatorType,
    AgEVeWayPtCompMethod,
)
from ansys.stk.core.stkutil import (
    AgECoordinateSystem,
    AgELineStyle,
    AgEOrbitStateType,
    AgEPositionType,
)
from ansys.stk.core.utilities.colors import Color, Colors


class STKTutorial:
    """Demonstrates how to set up a typical STK scenario using STK Engine."""

    def __init__(self):
        """Create a new instance and initialize the user interface."""
        self.stk = STKEngine.StartApplication(noGraphics=False)
        self.root = self.stk.NewObjectRoot()
        self.window = tk.Tk()
        self.window.title("STK Tutorial")
        self.window.protocol("WM_DELETE_WINDOW", self._exit)
        self.controlFrame = tk.Frame()
        self.mapControl = MapControl(self.controlFrame, width=640, height=360)
        self.mapControl.BackColor = Color.FromRGB(217, 217, 217)
        self.mapControl.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)
        self.globeControl = GlobeControl(
            self.controlFrame, width=640, height=360
        )
        self.globeControl.BackColor = Color.FromRGB(217, 217, 217)
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
        self.root.CloseScenario()
        self.window.destroy()
        self.stk.ShutDown()

    def _new_scenario(self):
        self.root.NewScenario("Tutorial")

        self._configure_units()
        self._configure_time_period()

        self.newScenarioBtn["state"] = "disabled"
        self.createFacilitiesBtn["state"] = "normal"

    def _configure_time_period(self):
        scenario = self.root.CurrentScenario

        scenario.SetTimePeriod(
            "1 Jul 2023 00:00:00.00", "1 Jul 2023 04:00:00.00"
        )
        scenario.Epoch = "1 Jul 2023 00:00:00.00"

    def _configure_units(self):
        dimensions = self.root.UnitPreferences
        dimensions.ResetUnits()
        dimensions.SetCurrentUnit("DateFormat", "UTCG")
        dimensions.SetCurrentUnit("DistanceUnit", "km")
        dimensions.SetCurrentUnit("TimeUnit", "sec")
        dimensions.SetCurrentUnit("AngleUnit", "deg")
        dimensions.SetCurrentUnit("MassUnit", "kg")
        dimensions.SetCurrentUnit("PowerUnit", "dbw")
        dimensions.SetCurrentUnit("FrequencyUnit", "ghz")
        dimensions.SetCurrentUnit("SmallDistanceUnit", "m")
        dimensions.SetCurrentUnit("latitudeUnit", "deg")
        dimensions.SetCurrentUnit("longitudeunit", "deg")
        dimensions.SetCurrentUnit("DurationUnit", "HMS")
        dimensions.SetCurrentUnit("Temperature", "K")
        dimensions.SetCurrentUnit("SmallTimeUnit", "sec")
        dimensions.SetCurrentUnit("RatioUnit", "db")
        dimensions.SetCurrentUnit("rcsUnit", "dbsm")
        dimensions.SetCurrentUnit("DopplerVelocityUnit", "m/s")
        dimensions.SetCurrentUnit("Percent", "unitValue")

    def _create_facilities(self):
        self.baikonur = self.root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "Baikonur"
        )
        self.baikonur.UseTerrain = False
        self.planetodetic = self.baikonur.Position.ConvertTo(
            AgEPositionType.ePlanetodetic
        )
        self.planetodetic.Lat = 48.0
        self.planetodetic.Lon = 55.0
        self.planetodetic.Alt = 0.0
        self.baikonur.Position.Assign(self.planetodetic)
        self.baikonur.ShortDescription = "Launch Site"
        self.baikonur.LongDescription = (
            "Launch site in Kazakhstan. Also known as Tyuratam."
        )

        self.perth = self.root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "Perth"
        )
        self.perth.UseTerrain = False
        self.planetodetic = self.perth.Position.ConvertTo(
            AgEPositionType.ePlanetodetic
        )
        self.planetodetic.Lat = -31.0
        self.planetodetic.Lon = 116.0
        self.planetodetic.Alt = 0
        self.perth.Position.Assign(self.planetodetic)
        self.perth.ShortDescription = "Australian Tracking Station"

        self.wallops = self.root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "Wallops"
        )
        self.wallops.UseTerrain = False
        self.planetodetic = self.wallops.Position.ConvertTo(
            AgEPositionType.ePlanetodetic
        )
        self.planetodetic.Lat = 37.8602
        self.planetodetic.Lon = -75.5095
        self.planetodetic.Alt = -0.0127878
        self.wallops.Position.Assign(self.planetodetic)
        self.wallops.ShortDescription = "NASA Launch Site/Tracking Station"

        result = self.root.ExecuteCommand("GetDirectory / Database Facility")
        facDataDir = result[0]
        filelocation = os.path.join(facDataDir, "stkFacility.fd")
        command = (
            'ImportFromDB * Facility "'
            + filelocation
            + '" Class Facility SiteName "Santiago Station AGO 3 STDN AGO3" '
            + 'Network "NASA NEN" Rename Santiago'
        )
        self.root.ExecuteCommand(command)
        command = (
            'ImportFromDB * Facility "'
            + filelocation
            + '" Class Facility SiteName "White Sands" '
            + 'Network "Other" Rename WhiteSands'
        )
        self.root.ExecuteCommand(command)

        self.santiago = self.root.CurrentScenario.Children["Santiago"]
        self.whitesands = self.root.CurrentScenario.Children["WhiteSands"]
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
        self.iceberg = self.root.CurrentScenario.Children.New(
            AgESTKObjectType.eTarget, "Iceberg"
        )
        self.iceberg.UseTerrain = False
        self.planetodetic = self.iceberg.Position.ConvertTo(
            AgEPositionType.ePlanetodetic
        )
        self.planetodetic.Lat = 74.91
        self.planetodetic.Lon = -74.5
        self.planetodetic.Alt = 0.0

        self.iceberg.Position.Assign(self.planetodetic)
        self.iceberg.ShortDescription = "Only the tip."
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
        cruise = self.root.CurrentScenario.Children.New(
            AgESTKObjectType.eShip, "Cruise"
        )
        cruise.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)
        greatArc = cruise.Route
        interval = greatArc.EphemerisInterval
        interval.SetExplicitInterval(
            "1 Jul 2023 00:00:00.00", interval.FindStopTime()
        )
        greatArc.Method = AgEVeWayPtCompMethod.eDetermineTimeAccFromVel

        self._add_waypoint(greatArc.Waypoints, 44.1, -8.5, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 51.0, -26.6, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 52.1, -40.1, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 60.2, -55.0, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 68.2, -65.0, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 72.5, -70.1, 0.0, 0.015, 0.0)
        self._add_waypoint(greatArc.Waypoints, 74.9, -74.5, 0.0, 0.015, 0.0)

        cruise.SetAttitudeType(AgEVeAttitude.eAttitudeStandard)
        attitude = cruise.Attitude
        attitude.Basic.SetProfileType(
            AgEVeProfile.eProfileECFVelocityAlignmentWithRadialConstraint
        )
        cruise.Graphics.WaypointMarker.IsWaypointMarkersVisible = True
        cruise.Graphics.WaypointMarker.IsTurnMarkersVisible = True
        greatArc.Propagate()
        self.root.Rewind()
        self.createShipBtn["state"] = "disabled"
        self.createSatellitesBtn["state"] = "normal"

    def _create_satellites(self):
        tdrs = self.root.CurrentScenario.Children.New(
            AgESTKObjectType.eSatellite, "TDRS"
        )
        tdrs.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        twobody = tdrs.Propagator

        classical = twobody.InitialState.Representation.ConvertTo(
            AgEOrbitStateType.eOrbitStateClassical
        )
        classical.CoordinateSystemType = (
            AgECoordinateSystem.eCoordinateSystemJ2000
        )
        interval = twobody.EphemerisInterval
        interval.SetExplicitInterval(
            "1 Jul 2023 00:00:00.000", "1 Jul 2023 04:00:00.000"
        )
        twobody.Step = 60
        classical.LocationType = AgEClassicalLocation.eLocationTrueAnomaly
        trueAnomaly = classical.Location
        trueAnomaly.Value = 178.845262

        classical.SizeShapeType = AgEClassicalSizeShape.eSizeShapePeriod
        period = classical.SizeShape
        period.Eccentricity = 0.0
        period.Period = 86164.090540
        classical.Orientation.ArgOfPerigee = 0.0
        classical.Orientation.Inclination = 0.0
        classical.Orientation.AscNodeType = AgEOrientationAscNode.eAscNodeLAN
        lan = classical.Orientation.AscNode
        lan.Value = 259.999982
        twobody.InitialState.Representation.Assign(classical)
        twobody.Propagate()

        result = self.root.ExecuteCommand("GetDirectory / Database Satellite")
        satDataDir = result[0]
        filelocation = os.path.join(satDataDir, "stkSatDb.sd")
        command = (
            'ImportFromDB * Satellite "'
            + filelocation
            + '" Rename TDRS_3 Propagate On CommonName "TDRS 3"'
        )
        self.root.ExecuteCommand(command)

        tdrsC = self.root.CurrentScenario.Children["TDRS_3"]
        sgp4 = tdrsC.Propagator
        interval = sgp4.EphemerisInterval
        interval.SetExplicitInterval(
            "1 Jul 2023 00:00:00.000", "1 Jul 2023 04:00:00.000"
        )

        self.ers1 = self.root.CurrentScenario.Children.New(
            AgESTKObjectType.eSatellite, "ERS1"
        )
        self.ers1.SetPropagatorType(
            AgEVePropagatorType.ePropagatorJ4Perturbation
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
            AgEOrbitStateType.eOrbitStateClassical
        )
        classical.CoordinateSystemType = (
            AgECoordinateSystem.eCoordinateSystemJ2000
        )
        classical.LocationType = AgEClassicalLocation.eLocationTrueAnomaly
        trueAnomaly = classical.Location
        trueAnomaly.Value = 0.0
        classical.SizeShapeType = AgEClassicalSizeShape.eSizeShapeSemimajorAxis
        semi = classical.SizeShape
        semi.SemiMajorAxis = 7163.14
        semi.Eccentricity = 0.0
        classical.Orientation.ArgOfPerigee = 0.0
        classical.Orientation.AscNodeType = AgEOrientationAscNode.eAscNodeLAN
        lan = classical.Orientation.AscNode
        lan.Value = 99.38
        classical.Orientation.Inclination = 98.50

        j4.InitialState.Representation.Assign(classical)
        j4.Propagate()
        self.root.Rewind()
        self.ers1.Graphics.Passes.VisibleSides = (
            AgEVeGfxVisibleSides.eVisibleSidesDescending
        )
        self.ers1.Graphics.Passes.VisibleSides = (
            AgEVeGfxVisibleSides.eVisibleSidesBoth
        )
        self.shuttle = self.root.CurrentScenario.Children.New(
            AgESTKObjectType.eSatellite, "Shuttle"
        )
        self.shuttle.SetPropagatorType(
            AgEVePropagatorType.ePropagatorJ4Perturbation
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
            AgEOrbitStateType.eOrbitStateClassical
        )
        classical.CoordinateSystemType = (
            AgECoordinateSystem.eCoordinateSystemJ2000
        )
        classical.LocationType = AgEClassicalLocation.eLocationTrueAnomaly
        trueAnomaly = classical.Location
        trueAnomaly.Value = 0.0
        classical.SizeShapeType = AgEClassicalSizeShape.eSizeShapeAltitude
        altitude = classical.SizeShape
        altitude.ApogeeAltitude = 370.4
        altitude.PerigeeAltitude = 370.4
        classical.Orientation.ArgOfPerigee = 0.0
        classical.Orientation.AscNodeType = AgEOrientationAscNode.eAscNodeLAN
        lan = classical.Orientation.AscNode
        lan.Value = -151.0
        classical.Orientation.Inclination = 28.5
        j4.InitialState.Representation.Assign(classical)

        j4.Propagate()
        self.root.Rewind()
        self.createSatellitesBtn["state"] = "disabled"
        self.shuttleContoursBtn["state"] = "normal"

    def _configure_shuttle_contours(self):
        self.shuttle.Graphics.SetAttributesType(
            AgEVeGfxAttributes.eAttributesBasic
        )
        orbitgfx = self.shuttle.Graphics.Attributes
        orbitgfx.Line.Style = AgELineStyle.eDashed
        orbitgfx.MarkerStyle = "Plus"

        contours = self.shuttle.Graphics.ElevContours
        elevations = contours.Elevations
        elevations.RemoveAll()
        elevations.AddLevelRange(0, 50, 10)

        for elem in elevations:
            elem.DistanceVisible = False
            elem.LineStyle = AgELineStyle.eDotDashed
            elem.LineWidth = AgELineWidth.e3

        contours.IsVisible = True
        self.root.Rewind()
        self.shuttleContoursBtn["state"] = "disabled"
        self.createAreaTargetsBtn["state"] = "normal"

    def _create_area_targets(self):
        self.searchArea = self.root.CurrentScenario.Children.New(
            AgESTKObjectType.eAreaTarget, "SearchArea"
        )
        atGfx = self.searchArea.Graphics
        atGfx.MarkerStyle = "None"
        atGfx.Inherit = False
        atGfx.LabelVisible = False
        atGfx.CentroidVisible = False

        self.searchArea.AutoCentroid = False
        self.searchArea.AreaType = AgEAreaType.ePattern
        patterns = self.searchArea.AreaTypeData
        patterns.Add(78.4399, -77.6125)
        patterns.Add(77.7879, -71.1578)
        patterns.Add(74.5279, -69.0714)
        patterns.Add(71.6591, -69.1316)
        patterns.Add(70.0291, -70.8318)
        patterns.Add(71.9851, -76.3086)

        self.searchArea.UseTerrainData = False
        sphere = self.searchArea.Position.ConvertTo(AgEPositionType.eSpherical)
        sphere.Lat = 74.9533
        sphere.Lon = -74.5482
        sphere.Radius = 6358.186790
        self.searchArea.Position.Assign(sphere)
        self.createAreaTargetsBtn["state"] = "disabled"
        self.accessBtn["state"] = "normal"

    def _compute_access(self):
        self.access = self.ers1.GetAccessToObject(self.searchArea)
        self.access.ComputeAccess()
        self.root.Rewind()

        interval = self.access.DataProviders["Access Data"]
        result = interval.Exec(
            "1 Jul 2023 00:00:00.000", "1 Jul 2023 04:00:00.000"
        )
        print("Access intervals:")
        for interval in result.Intervals:
            print(f"{interval.StartTime} {interval.StopTime}")

        self.accessBtn["state"] = "disabled"
        self.removeAccessBtn["state"] = "normal"

    def _remove_access(self):
        self.access.RemoveAccess()
        self.root.Rewind()
        self.removeAccessBtn["state"] = "disabled"
        self.createSensorsBtn["state"] = "normal"

    def _create_sensors(self):
        self.horizon = self.root.CurrentScenario.Children["ERS1"].Children.New(
            AgESTKObjectType.eSensor, "Horizon"
        )
        self.horizon.SetPatternType(AgESnPattern.eSnSimpleConic)
        simpleConic = self.horizon.Pattern
        simpleConic.ConeAngle = 90
        self.horizon.SetPointingType(AgESnPointing.eSnPtFixed)
        fixedPt = self.horizon.Pointing
        azEl = fixedPt.Orientation.ConvertTo(AgEOrientationType.eAzEl)
        azEl.Elevation = 90
        azEl.AboutBoresight = AgEAzElAboutBoresight.eAzElAboutBoresightRotate
        fixedPt.Orientation.Assign(azEl)

        # removing the ers1 elevcontours from the 2d window
        self.ers1.Graphics.ElevContours.IsVisible = False
        downlink = self.root.CurrentScenario.Children["ERS1"].Children.New(
            AgESTKObjectType.eSensor, "Downlink"
        )
        downlink.SetPatternType(AgESnPattern.eSnHalfPower)
        halfpower = downlink.Pattern
        halfpower.Frequency = 0.85
        halfpower.AntennaDiameter = 1.0

        downlink.SetPointingType(AgESnPointing.eSnPtTargeted)
        targeted = downlink.Pointing
        targeted.Boresight = AgESnPtTrgtBsightType.eSnPtTrgtBsightTracking
        targets = targeted.Targets
        targets.Add("Facility/Baikonur")
        targets.Add("Facility/WhiteSands")
        targets.Add("Facility/Perth")
        targets.AddObject(self.santiago)
        targets.Add(self.wallops.Path)

        self.root.Rewind()
        self.createSensorsBtn["state"] = "disabled"
        self.sensorVisibilityBtn["state"] = "normal"

    def _configure_sensor_visibility(self):
        fiveDegElev = self.root.CurrentScenario.Children[
            "Wallops"
        ].Children.New(AgESTKObjectType.eSensor, "FiveDegElev")

        fiveDegElev.SetPatternType(AgESnPattern.eSnComplexConic)
        complexConic = fiveDegElev.Pattern
        complexConic.InnerConeHalfAngle = 0
        complexConic.OuterConeHalfAngle = 85
        complexConic.MinimumClockAngle = 0
        complexConic.MaximumClockAngle = 360

        fiveDegElev.SetPointingType(AgESnPointing.eSnPtFixed)
        fixedPt = fiveDegElev.Pointing
        azEl = fixedPt.Orientation.ConvertTo(AgEOrientationType.eAzEl)
        azEl.Elevation = 90
        azEl.AboutBoresight = AgEAzElAboutBoresight.eAzElAboutBoresightRotate
        fixedPt.Orientation.Assign(azEl)

        fiveDegElev.Graphics.Projection.DistanceType = (
            AgESnProjectionDistanceType.eConstantAlt
        )
        dispDistance = fiveDegElev.Graphics.Projection.DistanceData
        dispDistance.Max = 785.248
        dispDistance.Min = 0
        dispDistance.NumberOfSteps = 1
        self.root.Rewind()
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
            AgEVeGfxAttributes.eAttributesCustom
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
        self.root.Rewind()
        self.displayIntervalsBtn["state"] = "disabled"
        self.accessIntervalsBtn["state"] = "normal"

    def _configure_access_intervals(self):
        self.ers1.Graphics.SetAttributesType(
            AgEVeGfxAttributes.eAttributesAccess
        )
        gfxAccess = self.ers1.Graphics.Attributes

        gfxAccess.AccessObjects.Add("Facility/Wallops")
        gfxAccess.AccessObjects.Add("Facility/Santiago")
        gfxAccess.AccessObjects.Add("Facility/Baikonur")
        gfxAccess.AccessObjects.Add("Facility/Perth")
        gfxAccess.AccessObjects.Add(self.whitesands.Path)

        orbitGfx = gfxAccess.NoAccess
        orbitGfx.IsVisible = True
        orbitGfx.Inherit = False
        orbitGfx.IsGroundMarkerVisible = False
        orbitGfx.IsOrbitMarkerVisible = False

        horizonDispTm = self.horizon
        horizonDispTm.SetDisplayStatusType(AgEDisplayTimesType.eDuringAccess)
        duringAccess = horizonDispTm.DisplayTimesData

        accessObjects = duringAccess.AccessObjects
        accessObjects.Add("Facility/Wallops")
        accessObjects.Add("Facility/Santiago")
        accessObjects.Add("Facility/Baikonur")
        accessObjects.AddObject(self.perth)
        accessObjects.Add(self.whitesands.Path)
        self.root.Rewind()
        self.accessIntervalsBtn["state"] = "disabled"
        self.rangeConstraintBtn["state"] = "normal"

    def _configure_range_constraints(self):
        access = self.horizon.GetAccessToObject(self.baikonur)
        access.ComputeAccess()
        minMax = self.horizon.AccessConstraints.AddConstraint(
            AgEAccessConstraints.eCstrRange
        )

        minMax.EnableMax = True
        minMax.Max = 2000
        minMax.Max = 1500
        minMax.Max = 1000
        minMax.Max = 500
        self.root.Rewind()
        self.rangeConstraintBtn["state"] = "disabled"


if __name__ == "__main__":
    stk_tutorial = STKTutorial()
    stk_tutorial.run()
