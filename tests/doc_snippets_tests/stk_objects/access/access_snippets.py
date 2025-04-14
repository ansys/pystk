# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys

from ansys.stk.core.stkobjects import (
    AberrationType,
    AccessConstraintType,
    AccessTimeType,
    ConstraintLighting,
    IvClockHost,
    IvTimeSense,
    OnePointAccessSummary,
    STKObjectType,
)
from ansys.stk.core.vgt import SmartIntervalState

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class AccessSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    def get_root(self):
        return CodeSnippetsTestBase.m_Root

    def get_scenario(self):
        return CodeSnippetsTestBase.m_Root.current_scenario

    def test_AccessConstraintsSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.AccessConstraintsSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="AccessConstraints",
        description="Get handle to the object access constraints",
        category="STK Objects | Access",
        eid="stkobjects~AccessConstraintCollection",
    )
    def AccessConstraintsSnippet(self, satellite):
        # Satellite satellite: Satellite object
        accessConstraints = satellite.access_constraints

    def test_AvailableAccessConstraintsSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            accessConstraints = parent.access_constraints

            self.AvailableAccessConstraintsSnippet(accessConstraints)
        finally:
            parent.unload()

    @code_snippet(
        name="AvailableAccessConstraints",
        description="Return a list of available constraints",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def AvailableAccessConstraintsSnippet(self, accessConstraints):
        # AccessConstraintCollection accessConstraints: Access Constraint collection
        constraintArray = accessConstraints.available_constraints()

        print("List of Available Constraints:")
        for i in range(0, len(constraintArray)):
            print(constraintArray[i])

    def test_AddLightingConstraintSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            accessConstraints = parent.access_constraints

            self.AddLightingConstraintSnippet(accessConstraints)
        finally:
            parent.unload()

    @code_snippet(
        name="AddLightingConstraint",
        description="Add and configure a lighting condition access constraint",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def AddLightingConstraintSnippet(self, accessConstraints):
        # AccessConstraintCollection accessConstraints: Access Constraint collection

        # Condition constraint
        light = accessConstraints.add_constraint(AccessConstraintType.LIGHTING)
        light.condition = ConstraintLighting.DIRECT_SUN

    def test_AddSunExclusionConstraintSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            accessConstraints = parent.access_constraints

            self.AddSunExclusionConstraintSnippet(accessConstraints)
        finally:
            parent.unload()

    @code_snippet(
        name="AddSunExclusionConstraint",
        description="Add and configure a Line Of Sight sun exclusion access constraint",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def AddSunExclusionConstraintSnippet(self, accessConstraints):
        # AccessConstraintCollection accessConstraints: Access Constraint collection

        # Angle constraint
        cnstrAngle = accessConstraints.add_constraint(AccessConstraintType.LIGHT_OF_SIGHT_SOLAR_EXCLUSION_ANGLE)
        cnstrAngle.angle = 176.0

    def test_AddLunarElevationAngleConstraintSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            accessConstraints = parent.access_constraints

            self.AddLunarElevationAngleConstraintSnippet(accessConstraints)
        finally:
            parent.unload()

    @code_snippet(
        name="AddLunarElevationAngleConstraint",
        description="Add and configure a lunar elevation angle access constraint",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def AddLunarElevationAngleConstraintSnippet(self, accessConstraints):
        # AccessConstraintCollection accessConstraints: Access Constraint collection

        # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
        minmax = accessConstraints.add_constraint(AccessConstraintType.LUNAR_ELEVATION_ANGLE)
        minmax.enable_minimum = True
        minmax.minimum = 11.1
        minmax.enable_maximum = True
        minmax.maximum = 88.8

    def test_AddSunElevationAngleConstraintSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            accessConstraints = parent.access_constraints

            self.AddSunElevationAngleConstraintSnippet(accessConstraints)
        finally:
            parent.unload()

    @code_snippet(
        name="AddSunElevationAngleConstraint",
        description="Add and configure a sun elevation angle access constraint",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def AddSunElevationAngleConstraintSnippet(self, accessConstraints):
        # AccessConstraintCollection accessConstraints: Access Constraint collection

        # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
        minmax = accessConstraints.add_constraint(AccessConstraintType.SUN_ELEVATION_ANGLE)
        minmax.enable_minimum = True
        minmax.minimum = 22.2
        minmax.enable_maximum = True
        minmax.maximum = 77.7

    def test_AddCbObstructionConstraintSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            accessConstraints = parent.access_constraints

            self.AddCbObstructionConstraintSnippet(accessConstraints)
        finally:
            parent.unload()

    @code_snippet(
        name="AddCbObstructionConstraint",
        description="Add and configure a central body obstruction access constraint",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def AddCbObstructionConstraintSnippet(self, accessConstraints):
        # AccessConstraintCollection accessConstraints: Access Constraint collection
        # Get IAgAccessCnstrCbObstruction interface
        cbObstrConstraint = accessConstraints.add_constraint(AccessConstraintType.CENTRAL_BODY_OBSTRUCTION)

        # AvailableObstructions returns a one dimensional array of obstruction paths
        availableArray = cbObstrConstraint.available_obstructions

        # In this example add all available obstructions
        print("Available obstructions")
        for i in range(0, len(availableArray)):
            print(availableArray[i])
            if availableArray[i] != "Sun":  # Sun is enabled by default
                cbObstrConstraint.add_obstruction(availableArray[i])

        # AssignedObstructions returns a one dimensional array of obstruction paths
        assignedArray = cbObstrConstraint.assigned_obstructions

        print("Assigned obstructions")
        for i in range(0, len(assignedArray)):
            print(assignedArray[i])

    def test_AddAltitudeConstraintSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            accessConstraints = parent.access_constraints

            self.AddAltitudeConstraintSnippet(accessConstraints)
        finally:
            parent.unload()

    @code_snippet(
        name="AddAltitudeConstraint",
        description="Add and configure an altitude access constraint",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def AddAltitudeConstraintSnippet(self, accessConstraints):
        # AccessConstraintCollection accessConstraints: Access Constraint collection

        # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
        # Attitude constraint
        altitude = accessConstraints.add_constraint(AccessConstraintType.ALTITUDE)
        altitude.enable_minimum = True
        altitude.minimum = 20.5  # km

    def test_AddMultipleConstraintSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            accessConstraints = parent.access_constraints

            self.AddMultipleConstraintSnippet(accessConstraints)
        finally:
            parent.unload()

    @code_snippet(
        name="AddMultipleConstraint",
        description="Add multiple access constraints of the same type to an STK Object",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def AddMultipleConstraintSnippet(self, accessConstraints):
        # AccessConstraintCollection accessConstraints: Access Constraint collection

        # Add constraints
        # Only the eCstrApparentTime (4), eCstrDuration (13), eCstrGMT (16), eCstrIntervals (22), eCstrLocalTime (27) constraint
        # types can be added multiple times to the constraint collection.
        time1 = accessConstraints.add_constraint(AccessConstraintType.LOCAL_TIME)
        time1.minimum = "00:00:00.000"
        time1.maximum = "23:00:00.000"

    def test_AddExclusionZoneConstraintSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            accessConstraints = parent.access_constraints

            self.AddExclusionZoneConstraintSnippet(accessConstraints)
        finally:
            parent.unload()

    @code_snippet(
        name="AddExclusionZoneConstraint",
        description="Add an Exclusion Zone access constraint",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def AddExclusionZoneConstraintSnippet(self, accessConstraints):
        # AccessConstraintCollection accessConstraints: Access Constraint collection
        excludeZone = accessConstraints.add_named_constraint("ExclusionZone")
        excludeZone.maximum_latitude = 45
        excludeZone.minimum_latitude = 15
        excludeZone.minimum_longitude = -75
        excludeZone.maximum_longitude = -35

    def test_RemoveAllConstraintsSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            accessConstraints = parent.access_constraints

            self.RemoveAllConstraintsSnippet(accessConstraints)
        finally:
            parent.unload()

    @code_snippet(
        name="RemoveAllConstraints",
        description="Remove all access constraints except for Line Of Sight",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def RemoveAllConstraintsSnippet(self, accessConstraints):
        # AccessConstraintCollection accessConstraints: Access Constraint collection
        for i in range(accessConstraints.count - 1, 0, -1):
            constraint = accessConstraints.Item(i).ConstraintName

            if (constraint == "LineOfSight") is False:
                if constraint == "ThirdBodyObstruction":
                    thirdBodyConstraint = accessConstraints.GetActiveNamedConstraint("ThirdBodyObstruction")
                    assignedArray = thirdBodyConstraint.AssignedObstructions

                    for j in range(0, len(assignedArray)):
                        thirdBodyConstraint.RemoveObstruction(assignedArray[j])

                elif constraint == "ExclusionZone":
                    accessConstraints.GetActiveNamedConstraint("ExclusionZone").RemoveAll()

                else:
                    accessConstraints.RemoveNamedConstraint(constraint)

    def test_ComputeAccessSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()
            facility = self.get_scenario().children.new(STKObjectType.FACILITY, "facility")

            self.ComputeAccessSnippet(satellite, facility)
        finally:
            satellite.unload()
            facility.unload()

    @code_snippet(
        name="ComputeAccess",
        description="Compute an access between two STK Objects (using IStkObject interface)",
        category="STK Objects | Access",
        eid="stkobjects~Access",
    )
    def ComputeAccessSnippet(self, satellite, facility):
        # Satellite satellite: Satellite object
        # Facility facility: Facility object

        # Get access by STK Object
        access = satellite.get_access_to_object(facility)

        # Compute access
        access.compute_access()

    def test_ComputeAccessPathsSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()
            MyFacility = self.get_scenario().children.new(STKObjectType.FACILITY, "MyFacility")

            self.ComputeAccessPathsSnippet(satellite)
        finally:
            satellite.unload()
            MyFacility.unload()

    @code_snippet(
        name="ComputeAccessPaths",
        description="Compute an access between two STK Objects (using object path)",
        category="STK Objects | Access",
        eid="stkobjects~Access",
    )
    def ComputeAccessPathsSnippet(self, satellite):
        # Satellite satellite: Satellite object

        # Get access by object path
        access = satellite.get_access("Facility/MyFacility")

        # Compute access
        access.compute_access()

    def test_ComputeAccessAdvancedSettingsSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            other_object = self.get_scenario().children.new(STKObjectType.SATELLITE, "accessOtherObject")
            other_object.propagator.propagate()
            access = parent.get_access(other_object.path)
            access.compute_access()

            self.ComputeAccessAdvancedSettingsSnippet(access)
        finally:
            parent.unload()
            other_object.unload()

    @code_snippet(
        name="ComputeAccessAdvancedSettings",
        description="Compute an Access with Advanced Settings",
        category="STK Objects | Access",
        eid="stkobjects~Access",
    )
    def ComputeAccessAdvancedSettingsSnippet(self, access):
        # Access access: Access object

        access.advanced.enable_light_time_delay = True
        access.advanced.time_light_delay_convergence = 0.00005
        access.advanced.aberration_type = AberrationType.ANNUAL
        access.advanced.use_default_clock_host_and_signal_sense = False
        access.advanced.clock_host = IvClockHost.BASE
        access.advanced.signal_sense_of_clock_host = IvTimeSense.TRANSMIT
        access.compute_access()

    def test_ComputeAccessPointSnippet(self):
        try:
            facility = self.get_scenario().children.new(STKObjectType.FACILITY, "facility")
            MySatellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "MySatellite")
            MySatellite.propagator.propagate()

            self.ComputeAccessPointSnippet(self.get_root(), facility)
        finally:
            facility.unload()
            MySatellite.unload()

    @code_snippet(
        name="ComputeAccessPoint",
        description="Compute an access for one point",
        category="STK Objects | Access",
        eid="stkobjects~OnePointAccess",
    )
    def ComputeAccessPointSnippet(self, root, facility):
        # IStkObject facility: Facility object
        onePtAccess = facility.create_one_point_access("Satellite/MySatellite")

        # Configure properties (if necessary)
        onePtAccess.start_time = root.current_scenario.start_time
        onePtAccess.stop_time = root.current_scenario.stop_time
        onePtAccess.step_size = 600
        onePtAccess.summary_option = OnePointAccessSummary.DETAILED

        # Compute results
        results = onePtAccess.compute()

        # Print results
        for i in range(0, results.count):
            result = results.item(i)
            print("Time: %s HasAccess: %s" % (result.time, str(result.access_is_satisfied)))

            for j in range(0, result.constraints.count):
                constraint = result.constraints.item(j)
                print(
                    "Constraint: %s Object: %s Status: %s Value:%s"
                    % (constraint.constraint, constraint.object_path, constraint.status, str(constraint.value))
                )

    def test_ExtractAccessIntervalsSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            other_object = self.get_scenario().children.new(STKObjectType.SATELLITE, "accessOtherObject")
            other_object.propagator.propagate()
            access = parent.get_access(other_object.path)
            access.compute_access()

            self.ExtractAccessIntervalsSnippet(access)
        finally:
            parent.unload()
            other_object.unload()

    @code_snippet(
        name="ExtractAccessIntervals",
        description="Compute and extract access interval times",
        category="STK Objects | Access",
        eid="stkobjects~Access",
    )
    def ExtractAccessIntervalsSnippet(self, access):
        # Access access: Access calculation
        # Get and display the Computed Access Intervals
        intervalCollection = access.computed_access_interval_times

        # Set the intervals to use to the Computed Access Intervals
        computedIntervals = intervalCollection.to_array(0, -1)
        access.specify_access_intervals(computedIntervals)

    def test_ConfigureAccessIntervalSnippet(self):
        try:
            MySatellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "MySatellite")
            MySatellite.propagator.propagate()
            MyFacility = self.get_scenario().children.new(STKObjectType.FACILITY, "MyFacility")

            self.ConfigureAccessIntervalSnippet(self.get_root())
        finally:
            MySatellite.unload()
            MyFacility.unload()

    @code_snippet(
        name="ConfigureAccessInterval",
        description="Configure the access analysis time period to specified time instants",
        category="STK Objects | Access",
        eid="stkobjects~Access",
    )
    def ConfigureAccessIntervalSnippet(self, root):
        # StkObjectRoot root: STK Object Model root

        satellite = root.get_object_from_path("Satellite/MySatellite")
        facility = root.get_object_from_path("Facility/MyFacility")

        # For this code snippet, let's use the time interval when the satellite reached min and max altitude values.
        # Note, this assumes time at min happens before time at max.
        timeOfAltMin = satellite.analysis_workbench_components.time_instants.item(
            "GroundTrajectory.Detic.LLA.Altitude.TimeOfMin"
        )
        timeOfAltMax = satellite.analysis_workbench_components.time_instants.item(
            "GroundTrajectory.Detic.LLA.Altitude.TimeOfMax"
        )

        # Set the access time period with the times we figured out above.
        access = satellite.get_access_to_object(facility)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod = access.access_time_period_data

        accessTimePeriod.access_interval.state = SmartIntervalState.START_STOP

        accessStartEpoch = accessTimePeriod.access_interval.get_start_epoch()
        accessStartEpoch.set_implicit_time(timeOfAltMin)
        accessTimePeriod.access_interval.set_start_epoch(accessStartEpoch)

        accessStopEpoch = accessTimePeriod.access_interval.get_stop_epoch()
        accessStopEpoch.set_implicit_time(timeOfAltMax)
        accessTimePeriod.access_interval.set_stop_epoch(accessStopEpoch)

    def test_ConfigureAccessIntervalAvailabilitySnippet(self):
        try:
            MySatellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "MySatellite")
            MySatellite.propagator.propagate()
            MyFacility = self.get_scenario().children.new(STKObjectType.FACILITY, "MyFacility")

            self.ConfigureAccessIntervalAvailabilitySnippet(self.get_root())
        finally:
            MySatellite.unload()
            MyFacility.unload()

    @code_snippet(
        name="ConfigureAccessIntervalAvailability",
        description="Configure the access interval to the availability time span of the object where access is being computed to",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def ConfigureAccessIntervalAvailabilitySnippet(self, root):
        # StkObjectRoot root: STK Object Model root

        satellite = root.get_object_from_path("Satellite/MySatellite")
        facility = root.get_object_from_path("Facility/MyFacility")
        access = satellite.get_access_to_object(facility)

        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod = access.access_time_period_data

        if satellite.analysis_workbench_components.time_intervals.contains("AvailabilityTimeSpan"):
            availabilityTimeSpan = satellite.analysis_workbench_components.time_intervals.item("AvailabilityTimeSpan")
            accessTimePeriod.access_interval.set_implicit_interval(availabilityTimeSpan)

    def test_GetAccessesSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            other_object = self.get_scenario().children.new(STKObjectType.SATELLITE, "accessOtherObject")
            other_object.propagator.propagate()
            access = parent.get_access(other_object.path)
            access.compute_access()

            self.GetAccessesSnippet(self.get_root())
        finally:
            parent.unload()
            other_object.unload()

    @code_snippet(
        name="GetAccesses",
        description="Get access between objects by path using the existing accesses",
        category="STK Objects | Access",
        eid="stkobjects~IAccessConstraint",
    )
    def GetAccessesSnippet(self, root):
        # StkObjectRoot root: STK Object Model root
        scenario = root.current_scenario
        accesses = scenario.get_existing_accesses()

        size = len(accesses)  # number of accesses

        object1 = accesses[0][0]  # e.g. "Satellite/MySatellite"
        object2 = accesses[0][1]  # e.g.  "Facility/MyFacility"
        computed = accesses[0][2]  # e.g. True  (if access has been computed)

        access = scenario.get_access_between_objects_by_path(object1, object2)
