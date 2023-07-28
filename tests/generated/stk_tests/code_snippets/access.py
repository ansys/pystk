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
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAndConfigureSunElevationAngleConstraint(stkobject.AccessConstraints)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def AddAndConfigureSunElevationAngleConstraint(self, accessConstraints: "IAccessConstraintCollection"):
        # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
        minmax: "IAccessConstraintMinMax" = clr.CastAs(
            accessConstraints.AddConstraint(AgEAccessConstraints.eCstrSunElevationAngle), IAccessConstraintMinMax
        )
        minmax.EnableMin = True
        minmax.Min = 22.2
        minmax.EnableMax = True
        minmax.Max = 77.7

    # endregion

    # region AddAndConfigureLunarElevationAngleConstraint
    def test_AddAndConfigureLunarElevationAngleConstraint(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAndConfigureLunarElevationAngleConstraint(stkobject.AccessConstraints)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def AddAndConfigureLunarElevationAngleConstraint(self, accessConstraints: "IAccessConstraintCollection"):
        # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
        minmax: "IAccessConstraintMinMax" = clr.CastAs(
            accessConstraints.AddConstraint(AgEAccessConstraints.eCstrLunarElevationAngle), IAccessConstraintMinMax
        )
        minmax.EnableMin = True
        minmax.Min = 11.1
        minmax.EnableMax = True
        minmax.Max = 88.8

    # endregion

    # region AddAndConfigureLOSSunExclConstraint
    def test_AddAndConfigureLOSSunExclConstraint(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAndConfigureLOSSunExclConstraint(stkobject.AccessConstraints)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def AddAndConfigureLOSSunExclConstraint(self, accessConstraints: "IAccessConstraintCollection"):
        # Angle constraint
        cnstrAngle: "IAccessConstraintAngle" = clr.CastAs(
            accessConstraints.AddConstraint(AgEAccessConstraints.eCstrLOSSunExclusion), IAccessConstraintAngle
        )
        cnstrAngle.Angle = 176.0

    # endregion

    # region AddAndConfigureLightingConstraint
    def test_AddAndConfigureLightingConstraint(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAndConfigureLightingConstraint(stkobject.AccessConstraints)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def AddAndConfigureLightingConstraint(self, accessConstraints: "IAccessConstraintCollection"):
        # Condition constraint
        light: "IAccessConstraintCondition" = clr.CastAs(
            accessConstraints.AddConstraint(AgEAccessConstraints.eCstrLighting), IAccessConstraintCondition
        )
        light.Condition = AgECnstrLighting.eDirectSun

    # endregion

    # region AddAndConfigureAltitudeConstraint
    def test_AddAndConfigureAltitudeConstraint(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAndConfigureAltitudeConstraint(stkobject.AccessConstraints)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def AddAndConfigureAltitudeConstraint(self, accessConstraints: "IAccessConstraintCollection"):
        # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
        # Attitude constraint
        altitude: "IAccessConstraintMinMax" = clr.CastAs(
            accessConstraints.AddConstraint(AgEAccessConstraints.eCstrAltitude), IAccessConstraintMinMax
        )
        altitude.EnableMin = True
        altitude.Min = 20.5

    # endregion

    # region AddAccessConstraintsToAnObject
    def test_AddAccessConstraintsToAnObject(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAccessConstraintsToAnObject(stkobject)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def AddAccessConstraintsToAnObject(self, stkobject: "IStkObject"):
        accessConstraints: "IAccessConstraintCollection" = stkobject.AccessConstraints

        # Add constraints
        accessConstraints.AddConstraint(AgEAccessConstraints.eCstrSunElevationAngle)

    # endregion

    # region RemoveAccessConstraintFromAnObject
    def test_RemoveAccessConstraintFromAnObject(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.RemoveAccessConstraintFromAnObject(stkobject)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def RemoveAccessConstraintFromAnObject(self, stkobject: "IStkObject"):
        accessConstraints: "IAccessConstraintCollection" = stkobject.AccessConstraints

        # Remove constraints
        accessConstraints.RemoveConstraint(AgEAccessConstraints.eCstrSunElevationAngle)

    # endregion

    # region AddAndConfigureThirdBodyObstructionConstraint
    def test_AddAndConfigureThirdBodyObstructionConstraint(self):
        satelliteName: str = "satellite1"
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eSatellite, satelliteName
        )
        self.AddAndConfigureThirdBodyObstructionConstraint(stkobject.AccessConstraints)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, satelliteName)

    def AddAndConfigureThirdBodyObstructionConstraint(self, accessconstraints: "IAccessConstraintCollection"):
        # Get IAgAccessCnstrThirdBody interface
        thirdBodyConstraint: "IAccessConstraintThirdBody" = clr.CastAs(
            accessconstraints.AddConstraint(AgEAccessConstraints.eCstrThirdBodyObstruction), IAccessConstraintThirdBody
        )

        # AvailableObstructions returns a one dimensional array of obstruction paths
        availableArray = thirdBodyConstraint.AvailableObstructions

        # In this example add all available obstructions
        Console.WriteLine("Available obstructions")
        available: str
        for available in availableArray:
            Console.WriteLine(available)
            thirdBodyConstraint.AddObstruction(available)

        # AssignedObstructions returns a one dimensional array of obstruction paths
        assignedArray = thirdBodyConstraint.AssignedObstructions

        Console.WriteLine("Assigned obstructions")
        assigned: str
        for assigned in assignedArray:
            Console.WriteLine(assigned)

    # endregion

    # region ListAllConstraintExclusiveZones
    def test_ListAllConstraintExclusiveZones(self):
        satelliteName: str = "satellite1"
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eSatellite, satelliteName
        )

        stkobject.AccessConstraints.AddConstraint(AgEAccessConstraints.eCstrExclusionZone)
        stkobject.AccessConstraints.AddConstraint(AgEAccessConstraints.eCstrExclusionZone)
        stkobject.AccessConstraints.AddConstraint(AgEAccessConstraints.eCstrExclusionZone)
        stkobject.AccessConstraints.AddConstraint(AgEAccessConstraints.eCstrExclusionZone)
        stkobject.AccessConstraints.AddConstraint(AgEAccessConstraints.eCstrExclusionZone)

        excZones: "IAccessConstraintExclZonesCollection" = clr.CastAs(
            stkobject.AccessConstraints.GetActiveConstraint(AgEAccessConstraints.eCstrExclusionZone),
            IAccessConstraintExclZonesCollection,
        )
        excZones.ChangeExclZone(0, -20, -30, 40, 50)
        excZones.ChangeExclZone(1, -10, 20, 10, 30)
        excZones.ChangeExclZone(2, -30, 30, -20, 10)
        excZones.ChangeExclZone(3, -40, -10, 0, 0)
        excZones.ChangeExclZone(4, -50, 0, 10, 20)

        self.ListAllConstraintExclusiveZones(stkobject.AccessConstraints)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, satelliteName)

    def ListAllConstraintExclusiveZones(self, accessconstraints: "IAccessConstraintCollection"):
        excZones: "IAccessConstraintExclZonesCollection" = clr.CastAs(
            accessconstraints.GetActiveConstraint(AgEAccessConstraints.eCstrExclusionZone),
            IAccessConstraintExclZonesCollection,
        )
        if excZones != None:
            # ToArray returns a two dimensional array
            # The second dimension is an array of minLon, minLat, maxLon, maxLat values
            zones = excZones.ToArray(0, -1)

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
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        fac: "IFacility" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1"), IFacility
        )
        sat.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        tb: "IVehiclePropagatorTwoBody" = clr.CastAs(sat.Propagator, IVehiclePropagatorTwoBody)
        tb.Propagate()
        fac.Position.AssignGeodetic(-34.88, -58.14, 0.0)  # so i can actually see the access on ui

        self.ComputeAccessBetweenTwoStkObjectsUsingObjectPath(clr.Convert(sat, IStkObject))
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "fac1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat1")

    def ComputeAccessBetweenTwoStkObjectsUsingObjectPath(self, stkObject: "IStkObject"):
        # Get access by object path
        access: "IStkAccess" = stkObject.GetAccess("Facility/fac1")

        # Compute access
        access.ComputeAccess()

    # endregion

    # region ComputeAccessBetweenTwoStkObjectsUsingIAgStkObjectInterface
    def test_ComputeAccessBetweenTwoStkObjectsUsingIAgStkObjectInterface(self):
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        fac: "IFacility" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1"), IFacility
        )
        sat.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        tb: "IVehiclePropagatorTwoBody" = clr.CastAs(sat.Propagator, IVehiclePropagatorTwoBody)
        tb.Propagate()
        fac.Position.AssignGeodetic(-34.88, -58.14, 0.0)  # so i can actually see the access on ui

        self.ComputeAccessBetweenTwoStkObjectsUsingIAgStkObjectInterface(
            clr.Convert(sat, IStkObject), clr.Convert(fac, IStkObject)
        )
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "fac1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat1")

    def ComputeAccessBetweenTwoStkObjectsUsingIAgStkObjectInterface(
        self, stkObject1: "IStkObject", stkObject2: "IStkObject"
    ):
        # Get access by STK Object
        access: "IStkAccess" = stkObject1.GetAccessToObject(stkObject2)

        # Compute access
        access.ComputeAccess()

    # endregion

    # region ComputeAccessIntervalTimes
    def test_ComputeAccessIntervalTimes(self):
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        fac: "IFacility" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1"), IFacility
        )
        sat.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        tb: "IVehiclePropagatorTwoBody" = clr.CastAs(sat.Propagator, IVehiclePropagatorTwoBody)
        tb.Propagate()
        fac.Position.AssignGeodetic(-34.88, -58.14, 0.0)  # so i can actually see the access on ui
        access: "IStkAccess" = (clr.CastAs(sat, IStkObject)).GetAccessToObject((clr.CastAs(fac, IStkObject)))
        access.ComputeAccess()

        self.ComputeAccessIntervalTimes(access)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "fac1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat1")

    def ComputeAccessIntervalTimes(self, access: "IStkAccess"):
        # Get and display the Computed Access Intervals
        intervalCollection: "IIntervalCollection" = access.ComputedAccessIntervalTimes

        # Set the intervals to use to the Computed Access Intervals
        computedIntervals = intervalCollection.ToArray(0, -1)
        access.SpecifyAccessIntervals(computedIntervals)

    # endregion

    # region CreateOnePtAccess
    def test_CreateOnePtAccess(self):
        fac: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1")
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "Satellite1"),
            ISatellite,
        )
        sat.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation)
        j2prop: "IVehiclePropagatorJ2Perturbation" = clr.CastAs(sat.Propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "1 Jan 2012 13:00:00.000")
        j2prop.Step = 60
        j2prop.Propagate()

        self.CreateOnePtAccess(fac)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "Satellite1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "fac1")

    def CreateOnePtAccess(self, facility: "IStkObject"):
        onePtAccess: "IOnePointAccess" = facility.CreateOnePointAccess("Satellite/Satellite1")

        # Configure properties (if necessary)
        onePtAccess.StartTime = "1 Jan 2012 12:00:00.000"
        onePtAccess.StopTime = "1 Jan 2012 13:00:00.000"
        onePtAccess.StepSize = 120
        onePtAccess.SummaryOption = AgEOnePtAccessSummary.eOnePtAccessSummaryDetailed

        # Compute results
        results: "IOnePointAccessResultCollection" = onePtAccess.Compute()

        i: int = 0
        while i < results.Count:
            result: "IOnePointAccessResult" = results[i]

            Console.WriteLine("Time: {0}, HasAccess: {1}", result.Time, result.AccessSatisfied)

            j: int = 0
            while j < result.Constraints.Count:
                constraint: "IOnePointAccessConstraint" = result.Constraints[j]
                Console.WriteLine(
                    "Constraint: {0}, Object {1}, Status {2}, Value {3}",
                    constraint.Constraint,
                    constraint.ObjectPath,
                    constraint.Status,
                    constraint.Value,
                )

                j += 1

            i += 1

    # endregion

    # region ComputeAccessAndGetConstraintDataFromDataProvider
    def test_ComputeAccessAndGetConstraintDataFromDataProvider(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "Satellite1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "Facility1")
        self.ComputeAccessAndGetConstraintDataFromDataProvider(CodeSnippetsTestBase.m_Root)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "Facility1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "Satellite1")

    def ComputeAccessAndGetConstraintDataFromDataProvider(self, root: "IStkObjectRoot"):
        # Compute Access between the facility and the satellite
        sat1: "IStkObject" = root.GetObjectFromPath("Satellite/Satellite1")
        fac1: "IStkObject" = root.GetObjectFromPath("Facility/Facility1")
        access: "IStkAccess" = sat1.GetAccessToObject(fac1)
        access.ComputeAccess()

        # Get the access intervals
        accessIntervals: "IIntervalCollection" = access.ComputedAccessIntervalTimes

        # Set unit preferences - change to get your preferred units
        root.UnitPreferences.SetCurrentUnit("Distance", "km")
        root.UnitPreferences.SetCurrentUnit("Angle", "deg")
        root.UnitPreferences.SetCurrentUnit("Time", "sec")
        root.UnitPreferences.SetCurrentUnit("DateFormat", "UTCG")

        # Extract the access intervals and the range information for each access interval
        dataPrvElements = ["Time", "FromAngularRate", "FromRange"]

        dp: "IDataProviderTimeVarying" = clr.CastAs(access.DataProviders["Constraint Data"], IDataProviderTimeVarying)

        index0: int = 0
        while index0 < accessIntervals.Count:
            startTime: typing.Any = None
            stopTime: typing.Any = None

            (startTime, stopTime) = accessIntervals.GetInterval(index0)

            Console.WriteLine("Access Interval #{0} - Start={1} Stop={2}", index0, startTime, stopTime)

            result: "IDataProviderResult" = dp.ExecElements(startTime, stopTime, 60, dataPrvElements)

            timeValues = result.DataSets[0].GetValues()
            fromAngularRateValues = result.DataSets[1].GetValues()
            fromRangeValues = result.DataSets[2].GetValues()

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
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.EnumerateAvailableConstraints(stkobject.AccessConstraints)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def EnumerateAvailableConstraints(self, accessConstraints: "IAccessConstraintCollection"):
        # The AvailableConstraints method returns a rectangular two-dimensional array of available constraints.
        # A row of the array consists of two elements where the first element is a symbolic name of the constraint,
        # and the second is a corresponding enumeration value.

        arAvailable = accessConstraints.AvailableConstraints()

        i: int = 0
        while i < len(arAvailable):
            availName: str = clr.Convert(arAvailable[i][0], str)
            eAccessConstraint: "AgEAccessConstraints" = clr.Convert(int(arAvailable[i][1]), AgEAccessConstraints)
            Console.WriteLine("\tConstraint {0}: {1} ({2})", i, availName, eAccessConstraint)

            i += 1

    # endregion

    # region ConfigureAccessTimePeriodUsingSmartInterval
    def test_ConfigureAccessTimePeriodUsingSmartInterval(self):
        scenario: "IStkObject" = TestBase.Application.CurrentScenario
        place: "IStkObject" = scenario.Children.New(AgESTKObjectType.ePlace, "ColoradoSprings")
        aircraft: "IStkObject" = scenario.Children.New(AgESTKObjectType.eAircraft, "UAV")
        aircraft.Children.New(AgESTKObjectType.eSensor, "UAVSensor")
        greatArc: "IVehiclePropagatorGreatArc" = clr.Convert(
            (clr.Convert(aircraft, IAircraft)).Route, IVehiclePropagatorGreatArc
        )

        waypoints = [
            [40.0399, -75.5973, 3.048, 0.077, 0],
            [40.0378, -75.5974, 3.048, 0.077, 0],
            [40.0387, -75.5976, 3.048, 0.077, 0],
        ]
        greatArc.SetPointsSmoothRateAndPropagate(waypoints)

        try:
            self.ConfigureAccessTimePeriodUsingSmartInterval(TestBase.Application)

        finally:
            aircraft.Unload()
            place.Unload()

    def ConfigureAccessTimePeriodUsingSmartInterval(self, stkRoot: "IStkObjectRoot"):
        uav: "IStkObject" = stkRoot.GetObjectFromPath("/Aircraft/UAV")
        sensor: "IStkObject" = stkRoot.GetObjectFromPath("/Aircraft/UAV/Sensor/UAVSensor")
        coloradoSprings: "IStkObject" = stkRoot.GetObjectFromPath("/Place/ColoradoSprings")

        # For this code snippet, let's use the time interval when the UAV reached min and max altitude values.
        # Note, this assumes time at min happens before time at max.
        timeOfAltMin: "ITimeToolEvent" = uav.Vgt.Events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMin"]
        timeOfAltMax: "ITimeToolEvent" = uav.Vgt.Events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMax"]

        # Set the access time period with the times we figured out above.
        access: "IStkAccess" = sensor.GetAccessToObject(coloradoSprings)
        access.AccessTimePeriod = AgEAccessTimeType.eUserSpecAccessTime
        accessTimePeriod: "IAccessTimePeriod" = clr.CastAs(access.AccessTimePeriodData, IAccessTimePeriod)

        accessTimePeriod.AccessInterval.State = AgECrdnSmartIntervalState.eCrdnSmartIntervalStateStartStop

        accessStartEpoch: "ITimeToolEventSmartEpoch" = accessTimePeriod.AccessInterval.GetStartEpoch()
        accessStartEpoch.SetImplicitTime(timeOfAltMin)
        accessTimePeriod.AccessInterval.SetStartEpoch(accessStartEpoch)

        accessStopEpoch: "ITimeToolEventSmartEpoch" = accessTimePeriod.AccessInterval.GetStopEpoch()
        accessStopEpoch.SetImplicitTime(timeOfAltMax)
        accessTimePeriod.AccessInterval.SetStopEpoch(accessStopEpoch)

    # endregion

    # region ConfigureAccessTimePeriodToObjectTimeOfOtherObject
    def test_ConfigureAccessTimePeriodToObjectTimeOfOtherObject(self):
        scenario: "IStkObject" = TestBase.Application.CurrentScenario
        satellite: "IStkObject" = scenario.Children.New(AgESTKObjectType.eSatellite, "GEO")
        twoBody: "IVehiclePropagatorTwoBody" = clr.Convert(
            (clr.Convert(satellite, ISatellite)).Propagator, IVehiclePropagatorTwoBody
        )
        twoBody.Propagate()

        aircraft: "IStkObject" = scenario.Children.New(AgESTKObjectType.eAircraft, "UAV")
        aircraft.Children.New(AgESTKObjectType.eSensor, "UAVSensor")
        greatArc: "IVehiclePropagatorGreatArc" = clr.Convert(
            (clr.Convert(aircraft, IAircraft)).Route, IVehiclePropagatorGreatArc
        )

        waypoints = [
            [40.0399, -75.5973, 3.048, 0.077, 0],
            [40.0378, -75.5974, 3.048, 0.077, 0],
            [40.0387, -75.5976, 3.048, 0.077, 0],
        ]
        greatArc.SetPointsSmoothRateAndPropagate(waypoints)

        try:
            self.ConfigureAccessTimePeriodToObjectTimeOfOtherObject(TestBase.Application)

        finally:
            aircraft.Unload()
            satellite.Unload()

    def ConfigureAccessTimePeriodToObjectTimeOfOtherObject(self, stkRoot: "IStkObjectRoot"):
        satellite: "IStkObject" = stkRoot.GetObjectFromPath("/Satellite/GEO")
        otherObject: "IStkObject" = stkRoot.GetObjectFromPath("/Aircraft/UAV/Sensor/UAVSensor")
        access: "IStkAccess" = satellite.GetAccessToObject(otherObject)

        access.AccessTimePeriod = AgEAccessTimeType.eUserSpecAccessTime
        accessTimePeriod: "IAccessTimePeriod" = clr.CastAs(access.AccessTimePeriodData, IAccessTimePeriod)
        if otherObject.Vgt.EventIntervals.Contains("AvailabilityTimeSpan"):
            availabilityTimeSpan: "ITimeToolEventInterval" = otherObject.Vgt.EventIntervals["AvailabilityTimeSpan"]
            accessTimePeriod.AccessInterval.SetImplicitInterval(availabilityTimeSpan)

    # endregion

    # region GetAccessBetweenObjectsByPathUsingGetExistingAccesses
    def test_GetAccessBetweenObjectsByPathUsingGetExistingAccesses(self):
        objFac: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "Fac1"
        )
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "Sat1"), ISatellite
        )
        sat.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        (clr.CastAs(sat.Propagator, IVehiclePropagatorTwoBody)).Propagate()

        access: "IStkAccess" = objFac.GetAccessToObject(clr.CastAs(sat, IStkObject))
        access.ComputeAccess()

        self.GetAccessBetweenObjectsByPathUsingGetExistingAccesses(CodeSnippetsTestBase.m_Root)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "Fac1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "Sat1")

    def GetAccessBetweenObjectsByPathUsingGetExistingAccesses(self, stkRoot: "IStkObjectRoot"):
        scenario: "IScenario" = clr.CastAs(stkRoot.CurrentScenario, IScenario)
        accesses = scenario.GetExistingAccesses()

        numAccesses: int = len(accesses)  # number of accesses

        object1: str = str(accesses[0][0])  # e.g. "Facility/Fac1"
        object2: str = str(accesses[0][1])  # e.g. "Satellite/Sat1"
        computed: bool = bool(accesses[0][2])  # e.g. true  (if access has been computed)

        access: "IStkAccess" = scenario.GetAccessBetweenObjectsByPath(object1, object2)

    # endregion

    # region AddMultipleAccessConstraintsOfTheSameTypeToAnObject
    def test_AddMultipleAccessConstraintsOfTheSameTypeToAnObject(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddMultipleAccessConstraintsOfTheSameTypeToAnObject(stkobject)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def AddMultipleAccessConstraintsOfTheSameTypeToAnObject(self, stkobject: "IStkObject"):
        accessConstraints: "IAccessConstraintCollection" = stkobject.AccessConstraints

        # Add constraints
        # Only the eCstrApparentTime, eCstrDuration, eCstrGMT, eCstrIntervals, eCstrLocalTime constraint
        # types can be added multiple times to the constraint collection.
        accessConstraints.AddConstraint(AgEAccessConstraints.eCstrLocalTime)
        accessConstraints.AddConstraint(AgEAccessConstraints.eCstrLocalTime)

    # endregion

    # region AddMultipleAWBAccessConstraintsOfTheSameTypeToAnObject
    def test_AddMultipleAWBAccessConstraintsOfTheSameTypeToAnObject(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddMultipleAWBAccessConstraintsOfTheSameTypeToAnObject(stkobject)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def AddMultipleAWBAccessConstraintsOfTheSameTypeToAnObject(self, stkobject: "IStkObject"):
        accessConstraints: "IAccessConstraintCollection" = stkobject.AccessConstraints
        awbAccessConstraints: "IAccessConstraintAnalysisWorkbenchCollection" = accessConstraints.AWBConstraints

        # Add constraints
        objectPath: str = (stkobject.ClassName + "/") + stkobject.InstanceName
        awbConst: "IAccessConstraintAnalysisWorkbench" = clr.CastAs(
            awbAccessConstraints.AddConstraint(
                AgEAWBAccessConstraints.eCstrAWBVectorMag, (objectPath + " East Vector")
            ),
            IAccessConstraintAnalysisWorkbench,
        )
        awbConst.EnableMin = True
        awbConst.Min = 0.0

        awbConst2: "IAccessConstraintAnalysisWorkbench" = clr.CastAs(
            awbAccessConstraints.AddConstraint(
                AgEAWBAccessConstraints.eCstrAWBVectorMag, (objectPath + " North Vector")
            ),
            IAccessConstraintAnalysisWorkbench,
        )
        awbConst2.EnableMax = True
        awbConst2.Max = 1000.0

    # endregion

    # region RemoveAWBAccessConstraint
    def test_RemoveAWBAccessConstraint(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        accessConstraints: "IAccessConstraintCollection" = stkobject.AccessConstraints
        awbAccessConstraints: "IAccessConstraintAnalysisWorkbenchCollection" = accessConstraints.AWBConstraints

        # Add constraints
        objectPath: str = (stkobject.ClassName + "/") + stkobject.InstanceName
        awbAccessConstraints.AddConstraint(AgEAWBAccessConstraints.eCstrAWBVectorMag, (objectPath + " East Vector"))
        self.RemoveAWBAccessConstraint(stkobject)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def RemoveAWBAccessConstraint(self, stkobject: "IStkObject"):
        accessConstraints: "IAccessConstraintCollection" = stkobject.AccessConstraints
        awbAccessConstraints: "IAccessConstraintAnalysisWorkbenchCollection" = accessConstraints.AWBConstraints

        objectPath: str = (stkobject.ClassName + "/") + stkobject.InstanceName
        awbAccessConstraints.RemoveConstraint(AgEAWBAccessConstraints.eCstrAWBVectorMag, (objectPath + " East Vector"))

    # endregion

    # region ListAllAWBConstraints
    def test_ListAllAWBConstraints(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        accessConstraints: "IAccessConstraintCollection" = stkobject.AccessConstraints
        awbAccessConstraints: "IAccessConstraintAnalysisWorkbenchCollection" = accessConstraints.AWBConstraints

        # Add constraints
        objectPath: str = (stkobject.ClassName + "/") + stkobject.InstanceName
        awbAccessConstraints.AddConstraint(AgEAWBAccessConstraints.eCstrAWBVectorMag, (objectPath + " East Vector"))
        awbAccessConstraints.AddConstraint(AgEAWBAccessConstraints.eCstrAWBAngle, (objectPath + " SunAzimuth Angle"))
        awbAccessConstraints.AddConstraint(
            AgEAWBAccessConstraints.eCstrAWBCondition, (objectPath + " BeforeStop Condition")
        )

        self.ListAllAWBConstraints(stkobject)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def ListAllAWBConstraints(self, stkobject: "IStkObject"):
        awbaccessconstraints: "IAccessConstraintAnalysisWorkbenchCollection" = (
            stkobject.AccessConstraints.AWBConstraints
        )
        awbConstraint: "IAccessConstraintAnalysisWorkbench"
        for awbConstraint in awbaccessconstraints:
            Console.WriteLine("Reference: {0}", awbConstraint.Reference)

    # endregion

    # region ListAllAvailableReferencesForAWBConstraintType
    def test_ListAllAvailableReferencesForAWBConstraintType(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.ListAllAvailableReferencesForAWBConstraintType(stkobject)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def ListAllAvailableReferencesForAWBConstraintType(self, stkobject: "IStkObject"):
        awbaccessconstraints: "IAccessConstraintAnalysisWorkbenchCollection" = (
            stkobject.AccessConstraints.AWBConstraints
        )
        availableReference: str
        for availableReference in awbaccessconstraints.GetAvailableReferences(AgEAWBAccessConstraints.eCstrAWBAngle):
            Console.WriteLine("Available Reference: {0}", availableReference)

    # endregion

    # region AddAWBAccessConstraintFromAWBComponent
    def test_AddAWBAccessConstraintFromAWBComponent(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )
        self.AddAWBAccessConstraintFromAWBComponent(stkobject)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def AddAWBAccessConstraintFromAWBComponent(self, stkobject: "IStkObject"):
        if stkobject.Vgt.Vectors.Contains("East"):
            vec: "IVectorGeometryToolVector" = stkobject.Vgt.Vectors["East"]
            crdnVec: "IAnalysisWorkbenchComponent" = clr.CastAs(vec, IAnalysisWorkbenchComponent)

            accessConstraints: "IAccessConstraintCollection" = stkobject.AccessConstraints
            awbAccessConstraints: "IAccessConstraintAnalysisWorkbenchCollection" = accessConstraints.AWBConstraints

            awbConst: "IAccessConstraintAnalysisWorkbench" = clr.CastAs(
                awbAccessConstraints.AddConstraint(AgEAWBAccessConstraints.eCstrAWBVectorMag, crdnVec.QualifiedPath),
                IAccessConstraintAnalysisWorkbench,
            )
            awbConst.EnableMin = True
            awbConst.Min = 0.0
            awbConst.EnableMax = True
            awbConst.Max = 1000.0

    # endregion
