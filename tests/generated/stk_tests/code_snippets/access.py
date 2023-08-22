from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class Access(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Access, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region AddAndConfigureSunElevationAngleConstraint
    def test_AddAndConfigureSunElevationAngleConstraint(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAndConfigureSunElevationAngleConstraint(stkobject.access_constraints)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def AddAndConfigureSunElevationAngleConstraint(self, accessConstraints: "IAccessConstraintCollection"):
        # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
        minmax: "IAccessConstraintMinMax" = clr.CastAs(
            accessConstraints.add_constraint(AgEAccessConstraints.eCstrSunElevationAngle), IAccessConstraintMinMax
        )
        minmax.enable_min = True
        minmax.min = 22.2
        minmax.enable_max = True
        minmax.max = 77.7

    # endregion

    # region AddAndConfigureLunarElevationAngleConstraint
    def test_AddAndConfigureLunarElevationAngleConstraint(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAndConfigureLunarElevationAngleConstraint(stkobject.access_constraints)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def AddAndConfigureLunarElevationAngleConstraint(self, accessConstraints: "IAccessConstraintCollection"):
        # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
        minmax: "IAccessConstraintMinMax" = clr.CastAs(
            accessConstraints.add_constraint(AgEAccessConstraints.eCstrLunarElevationAngle), IAccessConstraintMinMax
        )
        minmax.enable_min = True
        minmax.min = 11.1
        minmax.enable_max = True
        minmax.max = 88.8

    # endregion

    # region AddAndConfigureLOSSunExclConstraint
    def test_AddAndConfigureLOSSunExclConstraint(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAndConfigureLOSSunExclConstraint(stkobject.access_constraints)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def AddAndConfigureLOSSunExclConstraint(self, accessConstraints: "IAccessConstraintCollection"):
        # Angle constraint
        cnstrAngle: "IAccessConstraintAngle" = clr.CastAs(
            accessConstraints.add_constraint(AgEAccessConstraints.eCstrLOSSunExclusion), IAccessConstraintAngle
        )
        cnstrAngle.angle = 176.0

    # endregion

    # region AddAndConfigureLightingConstraint
    def test_AddAndConfigureLightingConstraint(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAndConfigureLightingConstraint(stkobject.access_constraints)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def AddAndConfigureLightingConstraint(self, accessConstraints: "IAccessConstraintCollection"):
        # Condition constraint
        light: "IAccessConstraintCondition" = clr.CastAs(
            accessConstraints.add_constraint(AgEAccessConstraints.eCstrLighting), IAccessConstraintCondition
        )
        light.condition = AgECnstrLighting.eDirectSun

    # endregion

    # region AddAndConfigureAltitudeConstraint
    def test_AddAndConfigureAltitudeConstraint(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAndConfigureAltitudeConstraint(stkobject.access_constraints)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def AddAndConfigureAltitudeConstraint(self, accessConstraints: "IAccessConstraintCollection"):
        # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
        # Attitude constraint
        altitude: "IAccessConstraintMinMax" = clr.CastAs(
            accessConstraints.add_constraint(AgEAccessConstraints.eCstrAltitude), IAccessConstraintMinMax
        )
        altitude.enable_min = True
        altitude.min = 20.5

    # endregion

    # region AddAccessConstraintsToAnObject
    def test_AddAccessConstraintsToAnObject(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAccessConstraintsToAnObject(stkobject)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def AddAccessConstraintsToAnObject(self, stkobject: "IStkObject"):
        accessConstraints: "IAccessConstraintCollection" = stkobject.access_constraints

        # Add constraints
        accessConstraints.add_constraint(AgEAccessConstraints.eCstrSunElevationAngle)

    # endregion

    # region RemoveAccessConstraintFromAnObject
    def test_RemoveAccessConstraintFromAnObject(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.RemoveAccessConstraintFromAnObject(stkobject)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def RemoveAccessConstraintFromAnObject(self, stkobject: "IStkObject"):
        accessConstraints: "IAccessConstraintCollection" = stkobject.access_constraints

        # Remove constraints
        accessConstraints.remove_constraint(AgEAccessConstraints.eCstrSunElevationAngle)

    # endregion

    # region AddAndConfigureThirdBodyObstructionConstraint
    def test_AddAndConfigureThirdBodyObstructionConstraint(self):
        satelliteName: str = "satellite1"
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eSatellite, satelliteName
        )
        self.AddAndConfigureThirdBodyObstructionConstraint(stkobject.access_constraints)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, satelliteName)

    def AddAndConfigureThirdBodyObstructionConstraint(self, accessconstraints: "IAccessConstraintCollection"):
        # Get IAccessConstraintThirdBody interface
        thirdBodyConstraint: "IAccessConstraintThirdBody" = clr.CastAs(
            accessconstraints.add_constraint(AgEAccessConstraints.eCstrThirdBodyObstruction), IAccessConstraintThirdBody
        )

        # AvailableObstructions returns a one dimensional array of obstruction paths
        availableArray = thirdBodyConstraint.available_obstructions

        # In this example add all available obstructions
        Console.WriteLine("Available obstructions")
        available: str
        for available in availableArray:
            Console.WriteLine(available)
            thirdBodyConstraint.add_obstruction(available)

        # AssignedObstructions returns a one dimensional array of obstruction paths
        assignedArray = thirdBodyConstraint.assigned_obstructions

        Console.WriteLine("Assigned obstructions")
        assigned: str
        for assigned in assignedArray:
            Console.WriteLine(assigned)

    # endregion

    # region ListAllConstraintExclusiveZones
    def test_ListAllConstraintExclusiveZones(self):
        satelliteName: str = "satellite1"
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eSatellite, satelliteName
        )

        stkobject.access_constraints.add_constraint(AgEAccessConstraints.eCstrExclusionZone)
        stkobject.access_constraints.add_constraint(AgEAccessConstraints.eCstrExclusionZone)
        stkobject.access_constraints.add_constraint(AgEAccessConstraints.eCstrExclusionZone)
        stkobject.access_constraints.add_constraint(AgEAccessConstraints.eCstrExclusionZone)
        stkobject.access_constraints.add_constraint(AgEAccessConstraints.eCstrExclusionZone)

        excZones: "IAccessConstraintExclZonesCollection" = clr.CastAs(
            stkobject.access_constraints.get_active_constraint(AgEAccessConstraints.eCstrExclusionZone),
            IAccessConstraintExclZonesCollection,
        )
        excZones.change_excl_zone(0, -20, -30, 40, 50)
        excZones.change_excl_zone(1, -10, 20, 10, 30)
        excZones.change_excl_zone(2, -30, 30, -20, 10)
        excZones.change_excl_zone(3, -40, -10, 0, 0)
        excZones.change_excl_zone(4, -50, 0, 10, 20)

        self.ListAllConstraintExclusiveZones(stkobject.access_constraints)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, satelliteName)

    def ListAllConstraintExclusiveZones(self, accessconstraints: "IAccessConstraintCollection"):
        excZones: "IAccessConstraintExclZonesCollection" = clr.CastAs(
            accessconstraints.get_active_constraint(AgEAccessConstraints.eCstrExclusionZone),
            IAccessConstraintExclZonesCollection,
        )
        if excZones != None:
            # ToArray returns a two dimensional array
            # The second dimension is an array of minLon, minLat, maxLon, maxLat values
            zones = excZones.to_array(0, -1)

            i: int = 0
            while i <= (len(zones) - 1):
                Console.WriteLine(
                    "MinLon: {0}, MinLat: {1}, MaxLon: {2}, MaxLat {3}",
                    zones[i][0],
                    zones[i][1],
                    zones[i][2],
                    zones[i][3],
                )

                i += 1

    # endregion

    # region ComputeAccessBetweenTwoStkObjectsUsingObjectPath
    def test_ComputeAccessBetweenTwoStkObjectsUsingObjectPath(self):
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        fac: "IFacility" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eFacility, "fac1"), IFacility
        )
        sat.set_propagator_type(AgEVePropagatorType.ePropagatorTwoBody)
        tb: "IVehiclePropagatorTwoBody" = clr.CastAs(sat.propagator, IVehiclePropagatorTwoBody)
        tb.propagate()
        fac.position.assign_geodetic(-34.88, -58.14, 0.0)  # so i can actually see the access on ui

        self.ComputeAccessBetweenTwoStkObjectsUsingObjectPath(clr.Convert(sat, IStkObject))
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "fac1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "sat1")

    def ComputeAccessBetweenTwoStkObjectsUsingObjectPath(self, stkObject: "IStkObject"):
        # Get access by object path
        access: "IStkAccess" = stkObject.get_access("Facility/fac1")

        # Compute access
        access.compute_access()

    # endregion

    # region ComputeAccessBetweenTwoStkObjectsUsingIAgStkObjectInterface
    def test_ComputeAccessBetweenTwoStkObjectsUsingIAgStkObjectInterface(self):
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        fac: "IFacility" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eFacility, "fac1"), IFacility
        )
        sat.set_propagator_type(AgEVePropagatorType.ePropagatorTwoBody)
        tb: "IVehiclePropagatorTwoBody" = clr.CastAs(sat.propagator, IVehiclePropagatorTwoBody)
        tb.propagate()
        fac.position.assign_geodetic(-34.88, -58.14, 0.0)  # so i can actually see the access on ui

        self.ComputeAccessBetweenTwoStkObjectsUsingIAgStkObjectInterface(
            clr.Convert(sat, IStkObject), clr.Convert(fac, IStkObject)
        )
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "fac1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "sat1")

    def ComputeAccessBetweenTwoStkObjectsUsingIAgStkObjectInterface(
        self, stkObject1: "IStkObject", stkObject2: "IStkObject"
    ):
        # Get access by STK Object
        access: "IStkAccess" = stkObject1.get_access_to_object(stkObject2)

        # Compute access
        access.compute_access()

    # endregion

    # region ComputeAccessIntervalTimes
    def test_ComputeAccessIntervalTimes(self):
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        fac: "IFacility" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eFacility, "fac1"), IFacility
        )
        sat.set_propagator_type(AgEVePropagatorType.ePropagatorTwoBody)
        tb: "IVehiclePropagatorTwoBody" = clr.CastAs(sat.propagator, IVehiclePropagatorTwoBody)
        tb.propagate()
        fac.position.assign_geodetic(-34.88, -58.14, 0.0)  # so i can actually see the access on ui
        access: "IStkAccess" = (clr.CastAs(sat, IStkObject)).get_access_to_object((clr.CastAs(fac, IStkObject)))
        access.compute_access()

        self.ComputeAccessIntervalTimes(access)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "fac1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "sat1")

    def ComputeAccessIntervalTimes(self, access: "IStkAccess"):
        # Get and display the Computed Access Intervals
        intervalCollection: "IIntervalCollection" = access.computed_access_interval_times

        # Set the intervals to use to the Computed Access Intervals
        computedIntervals = intervalCollection.to_array(0, -1)
        access.specify_access_intervals(computedIntervals)

    # endregion

    # region CreateOnePtAccess
    def test_CreateOnePtAccess(self):
        fac: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "fac1"
        )
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "Satellite1"),
            ISatellite,
        )
        sat.set_propagator_type(AgEVePropagatorType.ePropagatorJ2Perturbation)
        j2prop: "IVehiclePropagatorJ2Perturbation" = clr.CastAs(sat.propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "1 Jan 2012 13:00:00.000")
        j2prop.step = 60
        j2prop.propagate()

        self.CreateOnePtAccess(fac)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "Satellite1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "fac1")

    def CreateOnePtAccess(self, facility: "IStkObject"):
        onePtAccess: "IOnePointAccess" = facility.create_one_point_access("Satellite/Satellite1")

        # Configure properties (if necessary)
        onePtAccess.start_time = "1 Jan 2012 12:00:00.000"
        onePtAccess.stop_time = "1 Jan 2012 13:00:00.000"
        onePtAccess.step_size = 120
        onePtAccess.summary_option = AgEOnePtAccessSummary.eOnePtAccessSummaryDetailed

        # Compute results
        results: "IOnePointAccessResultCollection" = onePtAccess.compute()

        i: int = 0
        while i < results.count:
            result: "IOnePointAccessResult" = results[i]

            Console.WriteLine("Time: {0}, HasAccess: {1}", result.time, result.access_satisfied)

            j: int = 0
            while j < result.constraints.count:
                constraint: "IOnePointAccessConstraint" = result.constraints[j]
                Console.WriteLine(
                    "Constraint: {0}, Object {1}, Status {2}, Value {3}",
                    constraint.constraint,
                    constraint.object_path,
                    constraint.status,
                    constraint.value,
                )

                j += 1

            i += 1

    # endregion

    # region ComputeAccessAndGetConstraintDataFromDataProvider
    def test_ComputeAccessAndGetConstraintDataFromDataProvider(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "Satellite1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eFacility, "Facility1")
        self.ComputeAccessAndGetConstraintDataFromDataProvider(CodeSnippetsTestBase.m_Root)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "Facility1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "Satellite1")

    def ComputeAccessAndGetConstraintDataFromDataProvider(self, root: "IStkObjectRoot"):
        # Compute Access between the facility and the satellite
        sat1: "IStkObject" = root.get_object_from_path("Satellite/Satellite1")
        fac1: "IStkObject" = root.get_object_from_path("Facility/Facility1")
        access: "IStkAccess" = sat1.get_access_to_object(fac1)
        access.compute_access()

        # Get the access intervals
        accessIntervals: "IIntervalCollection" = access.computed_access_interval_times

        # Set unit preferences - change to get your preferred units
        root.unit_preferences.set_current_unit("Distance", "km")
        root.unit_preferences.set_current_unit("Angle", "deg")
        root.unit_preferences.set_current_unit("Time", "sec")
        root.unit_preferences.set_current_unit("DateFormat", "UTCG")

        # Extract the access intervals and the range information for each access interval
        dataPrvElements = ["Time", "FromAngularRate", "FromRange"]

        dp: "IDataProviderTimeVarying" = clr.CastAs(access.data_providers["Constraint Data"], IDataProviderTimeVarying)

        index0: int = 0
        while index0 < accessIntervals.count:
            startTime: typing.Any = None
            stopTime: typing.Any = None

            (startTime, stopTime) = accessIntervals.get_interval(index0)

            Console.WriteLine("Access Interval #{0} - Start={1} Stop={2}", index0, startTime, stopTime)

            result: "IDataProviderResult" = dp.exec_elements(startTime, stopTime, 60, dataPrvElements)

            timeValues = result.data_sets[0].get_values()
            fromAngularRateValues = result.data_sets[1].get_values()
            fromRangeValues = result.data_sets[2].get_values()

            index1: int = 0
            while index1 < len(timeValues):
                Console.WriteLine(
                    "{0}: FromAngularRate={1} FromRange={2}",
                    timeValues[index1],
                    fromAngularRateValues[index1],
                    fromRangeValues[index1],
                )

                index1 += 1

            Console.WriteLine()

            index0 += 1

    # endregion

    # region EnumerateAvailableConstraints
    def test_EnumerateAvailableConstraints(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.EnumerateAvailableConstraints(stkobject.access_constraints)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def EnumerateAvailableConstraints(self, accessConstraints: "IAccessConstraintCollection"):
        # The AvailableConstraints method returns a rectangular two-dimensional array of available constraints.
        # A row of the array consists of two elements where the first element is a symbolic name of the constraint,
        # and the second is a corresponding enumeration value.

        arAvailable = accessConstraints.available_constraints()

        i: int = 0
        while i < len(arAvailable):
            availName: str = clr.Convert(arAvailable[i][0], str)
            eAccessConstraint: "AgEAccessConstraints" = clr.Convert(int(arAvailable[i][1]), AgEAccessConstraints)
            Console.WriteLine("\tConstraint {0}: {1} ({2})", i, availName, eAccessConstraint)

            i += 1

    # endregion

    # region ConfigureAccessTimePeriodUsingSmartInterval
    def test_ConfigureAccessTimePeriodUsingSmartInterval(self):
        scenario: "IStkObject" = TestBase.Application.current_scenario
        place: "IStkObject" = scenario.children.new(AgESTKObjectType.ePlace, "ColoradoSprings")
        aircraft: "IStkObject" = scenario.children.new(AgESTKObjectType.eAircraft, "UAV")
        aircraft.children.new(AgESTKObjectType.eSensor, "UAVSensor")
        greatArc: "IVehiclePropagatorGreatArc" = clr.Convert(
            (clr.Convert(aircraft, IAircraft)).route, IVehiclePropagatorGreatArc
        )

        waypoints = [
            [40.0399, -75.5973, 3.048, 0.077, 0],
            [40.0378, -75.5974, 3.048, 0.077, 0],
            [40.0387, -75.5976, 3.048, 0.077, 0],
        ]
        greatArc.set_points_smooth_rate_and_propagate(waypoints)

        try:
            self.ConfigureAccessTimePeriodUsingSmartInterval(TestBase.Application)

        finally:
            aircraft.unload()
            place.unload()

    def ConfigureAccessTimePeriodUsingSmartInterval(self, stkRoot: "IStkObjectRoot"):
        uav: "IStkObject" = stkRoot.get_object_from_path("/Aircraft/UAV")
        sensor: "IStkObject" = stkRoot.get_object_from_path("/Aircraft/UAV/Sensor/UAVSensor")
        coloradoSprings: "IStkObject" = stkRoot.get_object_from_path("/Place/ColoradoSprings")

        # For this code snippet, let's use the time interval when the UAV reached min and max altitude values.
        # Note, this assumes time at min happens before time at max.
        timeOfAltMin: "ITimeToolEvent" = uav.vgt.events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMin"]
        timeOfAltMax: "ITimeToolEvent" = uav.vgt.events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMax"]

        # Set the access time period with the times we figured out above.
        access: "IStkAccess" = sensor.get_access_to_object(coloradoSprings)
        access.access_time_period = AgEAccessTimeType.eUserSpecAccessTime
        accessTimePeriod: "IAccessTimePeriod" = clr.CastAs(access.access_time_period_data, IAccessTimePeriod)

        accessTimePeriod.access_interval.state = AgECrdnSmartIntervalState.eCrdnSmartIntervalStateStartStop

        accessStartEpoch: "ITimeToolEventSmartEpoch" = accessTimePeriod.access_interval.get_start_epoch()
        accessStartEpoch.set_implicit_time(timeOfAltMin)
        accessTimePeriod.access_interval.set_start_epoch(accessStartEpoch)

        accessStopEpoch: "ITimeToolEventSmartEpoch" = accessTimePeriod.access_interval.get_stop_epoch()
        accessStopEpoch.set_implicit_time(timeOfAltMax)
        accessTimePeriod.access_interval.set_stop_epoch(accessStopEpoch)

    # endregion

    # region ConfigureAccessTimePeriodToObjectTimeOfOtherObject
    def test_ConfigureAccessTimePeriodToObjectTimeOfOtherObject(self):
        scenario: "IStkObject" = TestBase.Application.current_scenario
        satellite: "IStkObject" = scenario.children.new(AgESTKObjectType.eSatellite, "GEO")
        twoBody: "IVehiclePropagatorTwoBody" = clr.Convert(
            (clr.Convert(satellite, ISatellite)).propagator, IVehiclePropagatorTwoBody
        )
        twoBody.propagate()

        aircraft: "IStkObject" = scenario.children.new(AgESTKObjectType.eAircraft, "UAV")
        aircraft.children.new(AgESTKObjectType.eSensor, "UAVSensor")
        greatArc: "IVehiclePropagatorGreatArc" = clr.Convert(
            (clr.Convert(aircraft, IAircraft)).route, IVehiclePropagatorGreatArc
        )

        waypoints = [
            [40.0399, -75.5973, 3.048, 0.077, 0],
            [40.0378, -75.5974, 3.048, 0.077, 0],
            [40.0387, -75.5976, 3.048, 0.077, 0],
        ]
        greatArc.set_points_smooth_rate_and_propagate(waypoints)

        try:
            self.ConfigureAccessTimePeriodToObjectTimeOfOtherObject(TestBase.Application)

        finally:
            aircraft.unload()
            satellite.unload()

    def ConfigureAccessTimePeriodToObjectTimeOfOtherObject(self, stkRoot: "IStkObjectRoot"):
        satellite: "IStkObject" = stkRoot.get_object_from_path("/Satellite/GEO")
        otherObject: "IStkObject" = stkRoot.get_object_from_path("/Aircraft/UAV/Sensor/UAVSensor")
        access: "IStkAccess" = satellite.get_access_to_object(otherObject)

        access.access_time_period = AgEAccessTimeType.eUserSpecAccessTime
        accessTimePeriod: "IAccessTimePeriod" = clr.CastAs(access.access_time_period_data, IAccessTimePeriod)
        if otherObject.vgt.event_intervals.contains("AvailabilityTimeSpan"):
            availabilityTimeSpan: "ITimeToolEventInterval" = otherObject.vgt.event_intervals["AvailabilityTimeSpan"]
            accessTimePeriod.access_interval.set_implicit_interval(availabilityTimeSpan)

    # endregion

    # region GetAccessBetweenObjectsByPathUsingGetExistingAccesses
    def test_GetAccessBetweenObjectsByPathUsingGetExistingAccesses(self):
        objFac: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "Fac1"
        )
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "Sat1"), ISatellite
        )
        sat.set_propagator_type(AgEVePropagatorType.ePropagatorTwoBody)
        (clr.CastAs(sat.propagator, IVehiclePropagatorTwoBody)).propagate()

        access: "IStkAccess" = objFac.get_access_to_object(clr.CastAs(sat, IStkObject))
        access.compute_access()

        self.GetAccessBetweenObjectsByPathUsingGetExistingAccesses(CodeSnippetsTestBase.m_Root)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "Fac1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "Sat1")

    def GetAccessBetweenObjectsByPathUsingGetExistingAccesses(self, stkRoot: "IStkObjectRoot"):
        scenario: "IScenario" = clr.CastAs(stkRoot.current_scenario, IScenario)
        accesses = scenario.get_existing_accesses()

        numAccesses: int = len(accesses)  # number of accesses

        object1: str = str(accesses[0][0])  # e.g. "Facility/Fac1"
        object2: str = str(accesses[0][1])  # e.g. "Satellite/Sat1"
        computed: bool = bool(accesses[0][2])  # e.g. true  (if access has been computed)

        access: "IStkAccess" = scenario.get_access_between_objects_by_path(object1, object2)

    # endregion

    # region AddMultipleAccessConstraintsOfTheSameTypeToAnObject
    def test_AddMultipleAccessConstraintsOfTheSameTypeToAnObject(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddMultipleAccessConstraintsOfTheSameTypeToAnObject(stkobject)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def AddMultipleAccessConstraintsOfTheSameTypeToAnObject(self, stkobject: "IStkObject"):
        accessConstraints: "IAccessConstraintCollection" = stkobject.access_constraints

        # Add constraints
        # Only the eCstrApparentTime, eCstrDuration, eCstrGMT, eCstrIntervals, eCstrLocalTime constraint
        # types can be added multiple times to the constraint collection.
        accessConstraints.add_constraint(AgEAccessConstraints.eCstrLocalTime)
        accessConstraints.add_constraint(AgEAccessConstraints.eCstrLocalTime)

    # endregion

    # region AddMultipleAWBAccessConstraintsOfTheSameTypeToAnObject
    def test_AddMultipleAWBAccessConstraintsOfTheSameTypeToAnObject(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddMultipleAWBAccessConstraintsOfTheSameTypeToAnObject(stkobject)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def AddMultipleAWBAccessConstraintsOfTheSameTypeToAnObject(self, stkobject: "IStkObject"):
        accessConstraints: "IAccessConstraintCollection" = stkobject.access_constraints
        awbAccessConstraints: "IAccessConstraintAnalysisWorkbenchCollection" = accessConstraints.awb_constraints

        # Add constraints
        objectPath: str = (stkobject.class_name + "/") + stkobject.instance_name
        awbConst: "IAccessConstraintAnalysisWorkbench" = clr.CastAs(
            awbAccessConstraints.add_constraint(
                AgEAWBAccessConstraints.eCstrAWBVectorMag, (objectPath + " East Vector")
            ),
            IAccessConstraintAnalysisWorkbench,
        )
        awbConst.enable_min = True
        awbConst.min = 0.0

        awbConst2: "IAccessConstraintAnalysisWorkbench" = clr.CastAs(
            awbAccessConstraints.add_constraint(
                AgEAWBAccessConstraints.eCstrAWBVectorMag, (objectPath + " North Vector")
            ),
            IAccessConstraintAnalysisWorkbench,
        )
        awbConst2.enable_max = True
        awbConst2.max = 1000.0

    # endregion

    # region RemoveAWBAccessConstraint
    def test_RemoveAWBAccessConstraint(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        accessConstraints: "IAccessConstraintCollection" = stkobject.access_constraints
        awbAccessConstraints: "IAccessConstraintAnalysisWorkbenchCollection" = accessConstraints.awb_constraints

        # Add constraints
        objectPath: str = (stkobject.class_name + "/") + stkobject.instance_name
        awbAccessConstraints.add_constraint(AgEAWBAccessConstraints.eCstrAWBVectorMag, (objectPath + " East Vector"))
        self.RemoveAWBAccessConstraint(stkobject)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def RemoveAWBAccessConstraint(self, stkobject: "IStkObject"):
        accessConstraints: "IAccessConstraintCollection" = stkobject.access_constraints
        awbAccessConstraints: "IAccessConstraintAnalysisWorkbenchCollection" = accessConstraints.awb_constraints

        objectPath: str = (stkobject.class_name + "/") + stkobject.instance_name
        awbAccessConstraints.remove_constraint(AgEAWBAccessConstraints.eCstrAWBVectorMag, (objectPath + " East Vector"))

    # endregion

    # region ListAllAWBConstraints
    def test_ListAllAWBConstraints(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        accessConstraints: "IAccessConstraintCollection" = stkobject.access_constraints
        awbAccessConstraints: "IAccessConstraintAnalysisWorkbenchCollection" = accessConstraints.awb_constraints

        # Add constraints
        objectPath: str = (stkobject.class_name + "/") + stkobject.instance_name
        awbAccessConstraints.add_constraint(AgEAWBAccessConstraints.eCstrAWBVectorMag, (objectPath + " East Vector"))
        awbAccessConstraints.add_constraint(AgEAWBAccessConstraints.eCstrAWBAngle, (objectPath + " SunAzimuth Angle"))
        awbAccessConstraints.add_constraint(
            AgEAWBAccessConstraints.eCstrAWBCondition, (objectPath + " BeforeStop Condition")
        )

        self.ListAllAWBConstraints(stkobject)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def ListAllAWBConstraints(self, stkobject: "IStkObject"):
        awbaccessconstraints: "IAccessConstraintAnalysisWorkbenchCollection" = (
            stkobject.access_constraints.awb_constraints
        )
        awbConstraint: "IAccessConstraintAnalysisWorkbench"
        for awbConstraint in awbaccessconstraints:
            Console.WriteLine("Reference: {0}", awbConstraint.reference)

    # endregion

    # region ListAllAvailableReferencesForAWBConstraintType
    def test_ListAllAvailableReferencesForAWBConstraintType(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.ListAllAvailableReferencesForAWBConstraintType(stkobject)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def ListAllAvailableReferencesForAWBConstraintType(self, stkobject: "IStkObject"):
        awbaccessconstraints: "IAccessConstraintAnalysisWorkbenchCollection" = (
            stkobject.access_constraints.awb_constraints
        )
        availableReference: str
        for availableReference in awbaccessconstraints.get_available_references(AgEAWBAccessConstraints.eCstrAWBAngle):
            Console.WriteLine("Available Reference: {0}", availableReference)

    # endregion

    # region AddAWBAccessConstraintFromAWBComponent
    def test_AddAWBAccessConstraintFromAWBComponent(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAWBAccessConstraintFromAWBComponent(stkobject)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def AddAWBAccessConstraintFromAWBComponent(self, stkobject: "IStkObject"):
        if stkobject.vgt.vectors.contains("East"):
            vec: "IVectorGeometryToolVector" = stkobject.vgt.vectors["East"]
            crdnVec: "IAnalysisWorkbenchComponent" = clr.CastAs(vec, IAnalysisWorkbenchComponent)

            accessConstraints: "IAccessConstraintCollection" = stkobject.access_constraints
            awbAccessConstraints: "IAccessConstraintAnalysisWorkbenchCollection" = accessConstraints.awb_constraints

            awbConst: "IAccessConstraintAnalysisWorkbench" = clr.CastAs(
                awbAccessConstraints.add_constraint(AgEAWBAccessConstraints.eCstrAWBVectorMag, crdnVec.qualified_path),
                IAccessConstraintAnalysisWorkbench,
            )
            awbConst.enable_min = True
            awbConst.min = 0.0
            awbConst.enable_max = True
            awbConst.max = 1000.0

    # endregion
