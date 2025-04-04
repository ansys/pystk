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

from ansys.stk.core.stkobjects import STKObjectType

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase

class DataAnalysisSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    def get_scenario(self):
        return CodeSnippetsTestBase.m_Root.current_scenario

    def test_FlightProfileNumpyArraySnippet(self):
        try:
            aircraft = self.get_scenario().children.new(STKObjectType.AIRCRAFT, "aircraft")
            
            self.FlightProfileNumpyArraySnippet(aircraft)
        finally:
            aircraft.unload()

    @code_snippet(
        name="FlightProfileNumpyArray",
        description="Load a Numpy array with flight profile data",
        category="Data Analysis",
        eid="stkobjects~DataProviderResultDataSetCollection",
    )
    def FlightProfileNumpyArraySnippet(self, aircraft):
        # Aircraft aircraft: Aircraft object
        from scipy.spatial import ConvexHull
        import matplotlib.pyplot as plt

        # compute data provider results for an aircraft's Flight Profile By Time
        field_names = ['Mach #', 'Altitude']
        time_step_sec = 1.0

        flight_profile_data_provider = aircraft.data_providers.item('Flight Profile By Time')
        flight_profile_data = flight_profile_data_provider.execute_elements(self.get_scenario().start_time, self.get_scenario().stop_time, time_step_sec, field_names)

        # convert dataset collection in a row format as a Numpy array
        flight_profile_data_arr = flight_profile_data.data_sets.to_numpy_array()
        print(flight_profile_data_arr)

        # get shape of array (number of rows, number of columns)
        print(flight_profile_data_arr.shape)

        # plot estimated fligth envelope as a convex hull
        hull = ConvexHull(flight_profile_data_arr)

        plt.figure(figsize=(15,10))
        for simplex in hull.simplices:
            plt.plot(flight_profile_data_arr[simplex, 1], flight_profile_data_arr[simplex, 0], color="darkblue")

            plt.title('Estimated Flight Envelope', fontsize=15)
            plt.xlabel('Mach Number', fontsize=15)
            plt.ylabel('Altitude', fontsize=15)

            plt.tick_params(axis='x', labelsize=15)
            plt.tick_params(axis='y', labelsize=15)
            plt.grid()
    
    def test_CoverageDefinitionResultsToPandasDataFrameSnippet(self):
        try:
            coverage = self.get_scenario().children.new(STKObjectType.COVERAGE_DEFINITION, "coverage")

            self.CoverageDefinitionResultsToPandasDataFrameSnippet(coverage)
        finally:
            coverage.unload()

    @code_snippet(
        name="CoverageDefinitionResultsToPandasDataFrame",
        description="Convert coverage definition data provider results to a Pandas DataFrame",
        category="Data Analysis",
        eid="stkobjects~DataProviderResultDataSetCollection",
    )
    def CoverageDefinitionResultsToPandasDataFrameSnippet(self, coverage):
        # CoverageDefinition coverage: Coverage object
        # compute data provider results for All Regions by Pass coverage
        coverage_data_provider = coverage.data_providers.item('All Regions By Pass')
        coverage_data = coverage_data_provider.execute()

        # convert dataset collection in a row format as a Pandas DataFrame with default numeric row index
        coverage_arr = coverage_data.data_sets.to_pandas_dataframe()

    def test_AccessResultsToPandasDataFrameSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "MySatellite")
            satellite.propagator.propagate()
            facility = self.get_scenario().children.new(STKObjectType.FACILITY, "MyFacility")
            access = satellite.get_access(facility.path)
            access.compute_access()

            self.AccessResultsToPandasDataFrameSnippet(access)
        finally:
            satellite.unload()
            facility.unload()

    @code_snippet(
        name="AccessResultsToPandasDataFrame",
        description="Convert access data provider results to a Pandas DataFrame",
        category="Data Analysis",
        eid="stkobjects~DataProviderResultDataSetCollection",
    )
    def AccessResultsToPandasDataFrameSnippet(self, facility_satellite_access):
        # Access facility_satellite_access: Access calculation
        # compute data provider results for basic Access
        field_names = ['Access Number', 'Start Time', 'Stop Time', 'Duration']
        time_step_sec = 1.0

        access_data_provider = facility_satellite_access.data_providers.item('Access')
        access_data = access_data_provider.exec_elements(self.get_scenario().start_time, self.get_scenario().stop_time, time_step_sec, field_names)

        # convert dataset collection in a row format as a Pandas DataFrame
        index_column = 'Access Number'
        access_data_df = access_data.data_sets.to_pandas_dataframe(index_element_name=index_column)

    def test_DescriptiveStatisticsPandasDataFrameSnippet(self):
        try:
            coverage = self.get_scenario().children.new(STKObjectType.COVERAGE_DEFINITION, "coverage")

            self.DescriptiveStatisticsPandasDataFrameSnippet(coverage)
        finally:
            coverage.unload()

    @code_snippet(
        name="DescriptiveStatisticsPandasDataFrame",
        description="Compute descriptive statistics for access measurements using a Pandas DataFrame",
        category="Data Analysis",
        eid="stkobjects~DataProviderResultDataSetCollection",
    )
    def DescriptiveStatisticsPandasDataFrameSnippet(self, coverage):
        # CoverageDefinition coverage: Coverage object
        # compute data provider results for All Regions by Pass coverage
        coverage_data_provider = coverage.data_providers.item('All Regions By Pass')
        coverage_data = coverage_data_provider.execute()

        # convert dataset collection in a row format as a Pandas DataFrame with default numeric row index
        all_regions_coverage_df = coverage_data.data_sets.to_pandas_dataframe()

        # compute descriptive statistics of Duration, Percent Coverage, Area Coverage
        all_regions_coverage_df[['duration', 'percent coverage', 'area coverage']].describe()


    def test_CoverageDefinitionResultsPandasDataFrameHeatMapSnippet(self):
        try:
            coverage = self.get_scenario().children.new(STKObjectType.COVERAGE_DEFINITION, "coverage")

            self.CoverageDefinitionResultsPandasDataFrameHeatMapSnippet(coverage)
        finally:
            coverage.unload()

    @code_snippet(
        name="CoverageDefinitionResultsPandasDataFrameHeatMap",
        description="Create a heat map of coverage definition results graphing duration by asset using a Pandas DataFrame",
        category="Data Analysis",
        eid="stkobjects~DataProviderResultDataSetCollection",
    )
    def CoverageDefinitionResultsPandasDataFrameHeatMapSnippet(self, coverage):
        # CoverageDefinition coverage: Coverage object
        import seaborn as sns; sns.set_style('ticks')
        from matplotlib import pyplot as plt

        # compute data provider results for All Regions by Pass coverage
        coverage_data_provider = coverage.data_providers.item('All Regions By Pass')
        coverage_data = coverage_data_provider.execute()

        # convert dataset collection in a row format as a Pandas DataFrame with default numeric row index
        coverage_all_regions_elements = coverage_data_provider.elements
        all_regions_coverage_df = coverage_data.data_sets.to_pandas_dataframe(data_provider_elements=coverage_all_regions_elements)

        # reshape the DataFrame based on column values
        pivot = all_regions_coverage_df.pivot_table(index='region name', columns='asset name', values='duration')

        # plot heat map that shows duration by asset name by region
        plt.figure(figsize=(20,10))
        ax = sns.heatmap(pivot, cmap="YlGnBu")

        ax.set_xlabel('Duration by Asset', fontsize=20)
        ax.set_ylabel('Region Name', fontsize=20)
        plt.tick_params(axis='x', labelsize=15)
        plt.tick_params(axis='y', labelsize=15)