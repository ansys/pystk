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

from test_util import *

import unittest
import os

skip_test = False
test_skipped_msg = ""
try:
    import numpy as np
    import pandas as pd
except:
    skip_test = True
    test_skipped_msg = "STK DataAnalysis utility tests skipped because pandas or numpy installs could not be found."


class DataAnalysisUtilTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestBase.Initialize()

        TestBase.LoadTestScenario(os.path.join("APIDataAnalysisUtilTests", "APIDataAnalysisUtilTests.sc"))

    @classmethod
    def tearDownClass(cls):
        TestBase.Uninitialize()

    @unittest.skipIf(skip_test, test_skipped_msg)
    def test_to_numpy(self):
        world_coverage_def = "CoverageDefinition/World_Coverage"
        world_coverage_def = TestBase.root.get_object_from_path(world_coverage_def)

        # note, the coverage and access data provider results need to be reshaped be properly converted row
        # formatted numpy array
        all_regions_dprv: DataProviderFixed = world_coverage_def.data_providers.item("All Regions By Pass")
        all_regions_data: DataProviderResult = all_regions_dprv.execute()
        all_regions_data_sets: DataProviderResultDataSetCollection = all_regions_data.data_sets

        expected_results = all_regions_data_sets.to_numpy_array()
        expected_shape = (11352, 11)

        self.assertIsInstance(expected_results, np.ndarray)
        self.assertEqual(expected_results.shape, expected_shape)
        self.assertNotEqual(len(all_regions_data_sets.element_names), expected_shape[1])

    @unittest.skipIf(skip_test, test_skipped_msg)
    def test_to_numpy_results_not_reshaped(self):
        num_access_coverage = "*/CoverageDefinition/World_Coverage/FigureOfMerit/Num_Access_Coverage"
        num_access_coverage = TestBase.root.get_object_from_path(num_access_coverage)

        # note, FOM data is shaped properly without the need to reshape...this test ensures the data is still in the
        # proper format in the returned numpy array
        fom_dprv: DataProviderFixed = num_access_coverage.data_providers.item("FOM Definition")
        fom_dprv_data: DataProviderResult = fom_dprv.execute()
        fom_dprv_data_sets: DataProviderResultDataSetCollection = fom_dprv_data.data_sets

        expected_results = fom_dprv_data_sets.to_numpy_array()
        expected_shape = (3, 1)

        self.assertIsInstance(expected_results, np.ndarray)
        self.assertEqual(expected_results.shape, expected_shape)
        self.assertEqual(len(fom_dprv_data_sets.element_names), expected_shape[1])

    @unittest.skipIf(skip_test, test_skipped_msg)
    def test_to_numpy_empty_results_collection(self):
        world_coverage_def = "CoverageDefinition/World_Coverage"
        world_coverage_def = TestBase.root.get_object_from_path(world_coverage_def)

        scen: Scenario = TestBase.Application.current_scenario

        # query a data provider that returns an empty result set
        global_coverage_dprv: DataProviderFixed = world_coverage_def.data_providers.item("Global Coverage")
        global_coverage_data: DataProviderResult = global_coverage_dprv.execute(scen.start_time, scen.stop_time)
        global_coverage_data_sets: DataProviderResultDataSetCollection = global_coverage_data.data_sets

        expected_results = global_coverage_data_sets.to_numpy_array()
        expected_shape = (0,)

        self.assertIsInstance(expected_results, np.ndarray)
        self.assertEqual(expected_results.shape, expected_shape)

    @unittest.skipIf(skip_test, test_skipped_msg)
    def test_to_dataframe(self):
        world_coverage_def = "CoverageDefinition/World_Coverage"
        world_coverage_def = TestBase.root.get_object_from_path(world_coverage_def)

        # note, the coverage and access data provider results need to be reshaped be properly converted row
        # formatted numpy array
        all_regions_dprv: DataProviderFixed = world_coverage_def.data_providers.item("All Regions By Pass")
        all_regions_data: DataProviderResult = all_regions_dprv.execute()
        all_regions_data_sets: DataProviderResultDataSetCollection = all_regions_data.data_sets

        expected_results_df = all_regions_data_sets.to_pandas_dataframe()

        self.assertIsInstance(expected_results_df, pd.DataFrame)
        self.assertEqual(len(expected_results_df.index), 11352)
        self.assertEqual(len(expected_results_df.columns), 11)

    @unittest.skipIf(skip_test, test_skipped_msg)
    def test_to_dataframe_results_not_reshaped(self):
        num_access_coverage = "*/CoverageDefinition/World_Coverage/FigureOfMerit/Num_Access_Coverage"
        num_access_coverage = TestBase.root.get_object_from_path(num_access_coverage)

        # note, FOM data is shaped properly without the need to reshape...this test ensures the data is still in the
        # proper format in the returned pandas DataFrame
        fom_dprv: DataProviderFixed = num_access_coverage.data_providers.item("FOM Definition")
        fom_dprv_data: DataProviderResult = fom_dprv.execute()
        fom_dprv_data_sets: DataProviderResultDataSetCollection = fom_dprv_data.data_sets

        expected_results_df = fom_dprv_data_sets.to_pandas_dataframe()

        self.assertIsInstance(expected_results_df, pd.DataFrame)
        self.assertEqual(len(expected_results_df.index), 3)
        self.assertEqual(len(expected_results_df.columns), 1)

    @unittest.skipIf(skip_test, test_skipped_msg)
    def test_to_dataframe_empty_results_collection(self):
        world_coverage_def = "CoverageDefinition/World_Coverage"
        world_coverage_def = TestBase.root.get_object_from_path(world_coverage_def)

        scen: Scenario = TestBase.Application.current_scenario

        # query a data provider that returns an empty result set
        global_coverage_dprv: DataProviderFixed = world_coverage_def.data_providers.item("Global Coverage")
        global_coverage_data: DataProviderResult = global_coverage_dprv.execute(scen.start_time, scen.stop_time)
        global_coverage_data_sets: DataProviderResultDataSetCollection = global_coverage_data.data_sets

        expected_results_df = global_coverage_data_sets.to_pandas_dataframe()

        self.assertIsInstance(expected_results_df, pd.DataFrame)
        self.assertEqual(len(expected_results_df.index), 0)
        self.assertEqual(len(expected_results_df.columns), 0)

    @unittest.skipIf(skip_test, test_skipped_msg)
    def test_to_dataframe_set_index_column(self):
        num_access_coverage = "*/CoverageDefinition/World_Coverage/FigureOfMerit/Num_Access_Coverage"
        num_access_coverage = TestBase.root.get_object_from_path(num_access_coverage)

        region_stats_dprv: DataProviderFixed = num_access_coverage.data_providers.item("Region Stats")
        region_stats_data: DataProviderResult = region_stats_dprv.execute()
        region_stats_data_sets: DataProviderResultDataSetCollection = region_stats_data.data_sets

        index_element_name = "Region Name"

        expected_results_df = region_stats_data_sets.to_pandas_dataframe(index_element_name=index_element_name)

        self.assertIsInstance(expected_results_df, pd.DataFrame)
        self.assertEqual(len(expected_results_df.index), 288)
        self.assertEqual(len(expected_results_df.columns), 6)
        self.assertEqual(expected_results_df.index.name, "region name")

    @unittest.skipIf(skip_test, test_skipped_msg)
    def test_to_dataframe_raise_value_error_invalid_index_element_name(self):
        num_access_coverage = "*/CoverageDefinition/World_Coverage/FigureOfMerit/Num_Access_Coverage"
        num_access_coverage = TestBase.root.get_object_from_path(num_access_coverage)

        region_stats_dprv: DataProviderFixed = num_access_coverage.data_providers.item("Region Stats")
        region_stats_data: DataProviderResult = region_stats_dprv.execute()
        region_stats_data_sets: DataProviderResultDataSetCollection = region_stats_data.data_sets

        index_element_name = "Faux Invalid Element Name"

        with self.assertRaises(ValueError):
            expected_results_df = region_stats_data_sets.to_pandas_dataframe(index_element_name=index_element_name)

    @unittest.skipIf(skip_test, test_skipped_msg)
    def test_to_dataframe_map_types_to_dtypes(self):
        world_coverage_def = "CoverageDefinition/World_Coverage"
        world_coverage_def = TestBase.root.get_object_from_path(world_coverage_def)

        all_regions_dprv_as_dprv_fixed: DataProviderFixed = world_coverage_def.data_providers.item(
            "All Regions By Pass"
        )
        all_regions_data: DataProviderResult = all_regions_dprv_as_dprv_fixed.execute()
        all_regions_data_sets: DataProviderResultDataSetCollection = all_regions_data.data_sets

        all_regions_dprv_as_dprv: IDataProvider = IDataProvider(all_regions_dprv_as_dprv_fixed)
        all_regions_dprv_elements = all_regions_dprv_as_dprv.elements
        expected_results_df = all_regions_data_sets.to_pandas_dataframe(
            data_provider_elements=all_regions_dprv_elements
        )

        self.assertIsInstance(expected_results_df, pd.DataFrame)
        self.assertEqual(len(expected_results_df.index), 11352)
        self.assertEqual(len(expected_results_df.columns), 11)

        self.assertEqual(expected_results_df["region name"].dtype, "object")
        self.assertEqual(expected_results_df["access start"].dtype, "object")
        self.assertEqual(expected_results_df["asset full name"].dtype, "object")
        self.assertEqual(expected_results_df["area coverage"].dtype, "float64")
