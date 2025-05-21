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

"""
PySTK Data Provider Extensions.

A set of convenience utilities to facilitate the access and manipulation of STK data providers.
"""

import pandas as pd

from ansys.stk.core.stkobjects import DATA_PROVIDER_TYPE, Access, IStkObject


class DataProviderExtension(object):
    """Encapsulate the data and implementation necessary to simplify the process of accessing and manipulating data provider information."""

    def __init__(self, base_object: IStkObject) -> None:
        self.base_object = base_object
        pass

    def _get_fixed_data(self, provider_name, elements=None, pre_data=None):
        fixed_data_provider = self.base_object.data_providers.item(provider_name)
        if pre_data is not None:
            fixed_data_provider.pre_data = pre_data
        if elements is None:
            fixed_result = fixed_data_provider.execute()
        else:
            fixed_result = fixed_data_provider.execute_elements(elements)
        fixed_result_data = fixed_result.data_sets.to_pandas_dataframe()
        return fixed_result_data

    def _get_interval_data(self, provider_name, start_time, stop_time, elements=None, pre_data=None):
        interval_data_provider = self.base_object.data_providers.item(provider_name)
        if pre_data is not None:
            interval_data_provider.pre_data = pre_data
        if elements is None:
            interval_result = interval_data_provider.execute(start_time, stop_time)
        else:
            interval_result = interval_data_provider.execute_elements(start_time, stop_time, elements)
        interval_result_data = interval_result.data_sets.to_pandas_dataframe()
        return interval_result_data

    def _get_time_data(self, provider_name, start_time, stop_time, time_step, elements=None, pre_data=None):
        time_data_provider = self.base_object.data_providers.get_data_provider_time_varying_from_path(provider_name)
        if pre_data is not None:
            time_data_provider.pre_data = pre_data
        if elements is None:
            time_result = time_data_provider.execute(start_time, stop_time, time_step)
        else:
            time_result = time_data_provider.execute_elements(start_time, stop_time, time_step, elements)
        if time_result.sections.count > 0:
            # Process sections
            for x in range(0, time_result.sections.count):
                for y in range(0, time_result.sections[x].intervals.count):
                    row_data = time_result.sections[x].intervals[y].data_sets.to_pandas_dataframe()
                    row_data.insert(0, "Section", "")
                    row_data["Section"] = time_result.sections[x].title
                    # print(row_data)
                    if x == 0 and y == 0:
                        panda = row_data
                    else:
                        panda = pd.concat([panda, row_data], ignore_index=True)
            time_result_data = panda
        else:
            if time_result.intervals.count > 0:
                for i in range(0, time_result.intervals.count):
                    row = time_result.intervals[i].data_sets.to_pandas_dataframe()
                    if i > 0:
                        panda = pd.concat([panda, row], ignore_index=True)
                    else:
                        panda = row
                time_result_data = panda
            else:
                time_result_data = time_result.data_sets.to_pandas_dataframe()
        return time_result_data

    def get_pandas(self, provider_path, start_time=None, stop_time=None, time_step=None, elements=None, pre_data=None):
        """Return an object's data provider in the form of a Pandas DataFrame."""
        if isinstance(self.base_object, Access):
            root = self.base_object.target.root
        else:
            root = self.base_object.root
        scenario = root.current_scenario
        # To do: check if exists
        provider_info = self.base_object.data_providers.get_data_provider_information_from_path(provider_path)
        panda = None
        match provider_info.type:
            case DATA_PROVIDER_TYPE.FIXED:
                panda = self._get_fixed_data(self, provider_path, elements, pre_data)
                pass
            case DATA_PROVIDER_TYPE.INTERVAL:
                if start_time is None:
                    start_time = scenario.start_time
                if stop_time is None:
                    stop_time = scenario.stop_time
                panda = self._get_interval_data(self, provider_path, start_time, stop_time, elements, pre_data)
                pass
            case DATA_PROVIDER_TYPE.TIME_VARYING:
                if start_time is None:
                    start_time = scenario.start_time
                if stop_time is None:
                    stop_time = scenario.stop_time
                if time_step is None:
                    time_step = 60.0
                # panda = self._get_time_data(self, provider_path, start_time, stop_time, time_step, elements, pre_data)
                panda = self._get_time_data(provider_path, start_time, stop_time, time_step, elements, pre_data)
                pass

        return panda

    def get_value_at_time(self, time):
        """Return the value retrieved by indexing an object's data provider with a given time."""
        pass
