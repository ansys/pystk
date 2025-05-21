from asyncio.windows_events import NULL
import ansys.stk.core.stkobjects
import ansys.stk.core.vgt
from ansys.stk.core.stkobjects import IStkObject, DATA_PROVIDER_TYPE, Access
import pandas as pd


class data_provider_extension(object):
    def __init__(self, base_object:IStkObject) -> None:
        self.BaseObject = base_object
        pass
    
    def _get_fixed_data(self, provider_name, elements = None, pre_data = None):
        fixed_data_provider = self.BaseObject.data_providers.item(provider_name)
        if pre_data != None:
            fixed_data_provider.pre_data = pre_data
        if elements == None:
            fixed_result = fixed_data_provider.execute()
        else:
            fixed_result = fixed_data_provider.execute_elements(elements)
        fixed_result_data = fixed_result.data_sets.to_pandas_dataframe()
        return fixed_result_data
    
    def _get_interval_data(self,provider_name,start_time,stop_time, elements = None, pre_data = None):
        interval_data_provider = self.BaseObject.data_providers.item(provider_name)
        if pre_data != None:
            interval_data_provider.pre_data = pre_data
        if elements == None:
            interval_result = interval_data_provider.execute(start_time, stop_time)
        else:
            interval_result = interval_data_provider.execute_elements(start_time, stop_time, elements)
        interval_result_data = interval_result.data_sets.to_pandas_dataframe()
        return interval_result_data
    
    def _get_time_data(self,provider_name,start_time,stop_time,time_step, elements = None, pre_data = None):
        time_data_provider = self.BaseObject.data_providers.get_data_provider_time_varying_from_path(provider_name)
        if pre_data != None:
            time_data_provider.pre_data = pre_data
        if elements == None:
            time_result = time_data_provider.execute(start_time, stop_time, time_step)
        else:
            time_result = time_data_provider.execute_elements(start_time, stop_time, time_step, elements)
        if (time_result.sections.count > 0):
            #Process sections
            for x in range(0, time_result.sections.count):
                for y in range(0, time_result.sections[x].intervals.count):
                    row_data = time_result.sections[x].intervals[y].data_sets.to_pandas_dataframe();
                    row_data.insert(0,'Section','')
                    row_data['Section'] = time_result.sections[x].title
                    #print(row_data)
                    if x==0 and y==0:
                        panda = row_data
                    else:
                        panda = pd.concat([panda,row_data], ignore_index=True)
            time_result_data = panda
        else:
            if (time_result.intervals.count > 0):
                for i in range(0,time_result.intervals.count):
                    row = time_result.intervals[i].data_sets.to_pandas_dataframe()
                    if i > 0:
                        panda = pd.concat([panda,row], ignore_index=True)
                    else:
                        panda = row
                time_result_data = panda
            else:
                time_result_data = time_result.data_sets.to_pandas_dataframe()
        return time_result_data
    
    def get_pandas(self,provider_path,start_time = None,stop_time = None,time_step = None, elements = None, pre_data = None):
        if isinstance(self.BaseObject,Access):
            root = self.BaseObject.target.root
        else:
            root = self.BaseObject.root
        scenario = root.current_scenario
# To do: check if exists        
        provider_info = self.BaseObject.data_providers.get_data_provider_information_from_path(provider_path)       
        panda = None
        match provider_info.type:
            case DATA_PROVIDER_TYPE.FIXED:
                panda = self._get_fixed_data(self, provider_path, elements, pre_data)
                pass
            case DATA_PROVIDER_TYPE.INTERVAL:
                if start_time == None:
                    start_time = scenario.start_time
                if stop_time == None:
                    stop_time = scenario.stop_time
                panda = self._get_interval_data(self, provider_path, start_time, stop_time, elements, pre_data)
                pass
            case DATA_PROVIDER_TYPE.TIME_VARYING:
                if start_time == None:
                    start_time = scenario.start_time
                if stop_time == None:
                    stop_time = scenario.stop_time
                if time_step == None:
                    time_step = 60.0
                #panda = self._get_time_data(self, provider_path, start_time, stop_time, time_step, elements, pre_data)
                panda = self._get_time_data(provider_path, start_time, stop_time, time_step, elements, pre_data)
                pass          
        
        return panda
    
    def get_value_at_time(time):
        pass
            
