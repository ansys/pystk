# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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

from ansys.stk.core.stkobjects import STKObjectType

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class DataProvidersSnippets(CodeSnippetsTestBase):
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

    def test_IntervalDataProviderSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()
            facility = self.get_scenario().children.new(STKObjectType.FACILITY, "facility")

            self.IntervalDataProviderSnippet(self.get_root(), satellite, facility)
        finally:
            satellite.unload()
            facility.unload()

    @code_snippet(
        name="IntervalDataProvider",
        description="Use an interval Data Provider",
        category="STK Objects | Data Providers",
        eid="stkobjects~DataProviderCollection",
    )
    def IntervalDataProviderSnippet(self, root, satellite, facility):
        # StkObjectRoot root: STK Object Model root
        # Satellite satellite: Satellite object
        # Facility facility: Facility object

        # Change DateFormat dimension to epoch seconds to make the data easier to handle in
        # Python
        root.units_preferences.item("DateFormat").set_current_unit("EpSec")
        # Get the current scenario
        scenario = root.current_scenario
        # Set up the access object
        access = satellite.get_access_to_object(facility)
        access.compute_access()
        # Get the Access AER Data Provider
        accessDP = access.data_providers.item("Access Data").execute(scenario.start_time, scenario.stop_time)

        accessStartTimes = accessDP.data_sets.get_data_set_by_name("Start Time").get_values()
        accessStopTimes = accessDP.data_sets.get_data_set_by_name("Stop Time").get_values()

    def test_TimeDependentDataProviderElementsSnippet(self):
        try:
            scenario = self.get_scenario()
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.TimeDependentDataProviderElementsSnippet(self.get_root(), scenario, satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="TimeDependentDataProviderElements",
        description="Use a Time Dependent Data Provider and requesting only specified elements",
        category="STK Objects | Data Providers",
        eid="stkobjects~DataProviderCollection",
    )
    def TimeDependentDataProviderElementsSnippet(self, root, scenario, satellite):
        # StkObjectRoot root: STK Object Model root
        # Satellite satellite: Satellite object
        # Scenario scenario: Scenario object
        # Change DateFormat dimension to epoch seconds to make the data easier to handle in
        # Python
        root.units_preferences.item("DateFormat").set_current_unit("EpSec")
        elems = [["Time"], ["q1"], ["q2"], ["q3"], ["q4"]]
        satDP = satellite.data_providers.item("Attitude Quaternions").execute_elements(
            scenario.start_time, scenario.stop_time, 60, elems
        )
        # Whenever you pass an index to an array, you need to cast it to a long
        # equivalent (int32)
        satTime = satDP.data_sets.item(0).get_values()
        satq1 = satDP.data_sets.item(1).get_values()
        satq2 = satDP.data_sets.item(2).get_values()
        satq3 = satDP.data_sets.item(3).get_values()
        satq4 = satDP.data_sets.item(4).get_values()

    def test_GroupsDataProviderSnippet(self):
        try:
            scenario = self.get_scenario()
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GroupsDataProviderSnippet(self.get_root(), scenario, satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GroupsDataProvider",
        description="Extract Elements from Data Providers with Groups",
        category="STK Objects | Data Providers",
        eid="stkobjects~DataProviderCollection",
    )
    def GroupsDataProviderSnippet(self, root, scenario, satellite):
        # StkObjectRoot root: STK Object Model root
        # Satellite satellite: Satellite object
        # Scenario scenario: Scenario object
        # Change DateFormat dimension to epoch seconds to make the data easier to handle in
        # Python
        root.units_preferences.item("DateFormat").set_current_unit("EpSec")
        satPosDP = (
            satellite.data_providers.item("Cartesian Position")
            .group.item("ICRF")
            .execute(scenario.start_time, scenario.stop_time, 60)
        )
        satx = satPosDP.data_sets.get_data_set_by_name("x").get_values()
        saty = satPosDP.data_sets.get_data_set_by_name("y").get_values()
        satz = satPosDP.data_sets.get_data_set_by_name("z").get_values()

        satVelDP = satellite.data_providers.get_data_provider_time_varying_from_path("Cartesian Velocity/ICRF").execute(
            scenario.start_time, scenario.stop_time, 60
        )
        # There are 4 Methods to get DP From a Path depending on the kind of DP:
        #   GetDataPrvTimeVarFromPath
        #   GetDataPrvIntervalFromPath
        #   GetDataPrvInfoFromPath
        #   GetDataPrvFixedFromPath
        satvx = satVelDP.data_sets.get_data_set_by_name("x").get_values()
        satvy = satVelDP.data_sets.get_data_set_by_name("y").get_values()
        satvz = satVelDP.data_sets.get_data_set_by_name("z").get_values()

    def test_DataProviderPreDataSnippet(self):
        try:
            scenario = self.get_scenario()
            facility = self.get_scenario().children.new(STKObjectType.FACILITY, "facility")

            self.DataProviderPreDataSnippet(self.get_root(), scenario, facility)
        finally:
            facility.unload()

    @code_snippet(
        name="DataProviderPreData",
        description="Extract Elements from Data Providers with pre-data",
        category="STK Objects | Data Providers",
        eid="stkobjects~DataProviderCollection",
    )
    def DataProviderPreDataSnippet(self, root, scenario, facility):
        # StkObjectRoot root: STK Object Model root
        # Facility facility: Facility object
        # Scenario scenario: Scenario object
        # Change DateFormat dimension to epoch seconds to make the data easier to handle in
        # Python
        root.units_preferences.item("DateFormat").set_current_unit("EpSec")
        facChooseDP = facility.data_providers.item("Points Choose System")
        dataProvCenter = facChooseDP.group.item("Center")
        # Choose the reference system you want to report the Center point in
        dataProvCenter.pre_data = "CentralBody/Earth TOD"
        rptElems = [["Time"], ["x"], ["y"], ["z"]]
        results = dataProvCenter.execute_elements(scenario.start_time, scenario.stop_time, 60, rptElems)
        datasets = results.data_sets
        Time = datasets.get_data_set_by_name("Time").get_values()
        facTODx = datasets.get_data_set_by_name("x").get_values()
        facTODy = datasets.get_data_set_by_name("y").get_values()
        facTODz = datasets.get_data_set_by_name("z").get_values()

    def test_SingleTimeDataProviderSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.SingleTimeDataProviderSnippet(self.get_root(), satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="SingleTimeDataProvider",
        description="Get Data for a Single Point in Time",
        category="STK Objects | Data Providers",
        eid="stkobjects~DataProviderCollection",
    )
    def SingleTimeDataProviderSnippet(self, root, satellite):
        # StkObjectRoot root: STK Object Model root
        # Satellite satellite: Satellite object
        # Change DateFormat dimension to epoch seconds to make the data easier to handle in
        # Python
        root.units_preferences.item("DateFormat").set_current_unit("EpSec")
        satPassDP = satellite.data_providers.item("Precision Passes").execute_single(2600)
        passes = satPassDP.data_sets.get_data_set_by_name("Precision Pass Number").get_values()

    def test_SingleTimesDataProviderSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.SingleTimesDataProviderSnippet(self.get_root(), satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="SingleTimesDataProvider",
        description="Get Data for Specific Points and Elements",
        category="STK Objects | Data Providers",
        eid="stkobjects~DataProviderCollection",
    )
    def SingleTimesDataProviderSnippet(self, root, satellite):
        # StkObjectRoot root: STK Object Model root
        # Satellite satellite: Satellite object
        # Change DateFormat dimension to epoch seconds to make the data easier to handle in
        # Python
        root.units_preferences.item("DateFormat").set_current_unit("EpSec")
        times = [[0], [15000], [20000], [55000]]
        elems = [["Time"], ["Precision Pass Number"]]
        satPassesDP = satellite.data_providers.item("Precision Passes").execute_single_elements_array(times, elems)
        passes = satPassesDP.get_array(1)
