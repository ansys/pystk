from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def aer_graphical_time_xy_graph(stk_obj : StkAccess, start_time=None, stop_time=None, step=60):
    root = stk_obj.base.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time

    df = stk_obj.data_providers.item('AER Data').group.item("Default").exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': False, 'ylog10': False, 'y2log10': False, 'label': 'Longitude/Angle', 'lines': [
            {'y_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': False, 'unit_pref': 'Longitude'}, 
            {'y_name':'elevation', 'label':'Elevation', 'use_unit':True, 'unit_squared': False, 'unit_pref' : 'Angle'}]},

            {'use_unit' : True, 'unit_squared': False, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'range', 'label':'Range', 'use_unit':True, 'unit_squared': False, 'unit_pref':'Distance'}]}]
    numerical_columns = ['azimuth','elevation','range']
    time_columns = ['time']
    title = 'AER'
    
    return line_chart_time_x(df, root, numerical_columns, time_columns, axes, title, groupby='access number')


def az_el_polar_graphical_polar_center_90_graph(stk_obj : StkAccess, start_time=None, stop_time=None, step=60):
    root = stk_obj.base.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time

    df = stk_obj.data_providers.item('AER Data').group.item("Default").exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axis ={'use_unit': True, 'unit_squared': False, 'label': 'Angle', 'lines': [
        {'y_name': 'elevation', 'x_name' : 'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': False, 'unit_pref': 'Angle'},
    ]}

    numerical_columns = ['elevation','azimuth']
    title = 'Az El Polar'
    return polar_chart(df, root, numerical_columns, 'Azimuth', 'azimuth', axis, title, origin_0 = False, groupby='access number', convert_negative_r=False)

def access_times_graphical_interval_graph(stk_obj : StkAccess, start_time=None, stop_time=None):
    root = stk_obj.base.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    
    df = stk_obj.data_providers.item('Access Data').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    elements=[(('start time', '0'),('stop time', '0'))]
    return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Access Times')

def access_duration_graphical_pie_graph(stk_obj : StkAccess, start_time=None, stop_time=None):
    root = stk_obj.base.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    
    df = stk_obj.data_providers.item('Access Data').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    return pie_chart(root, df, ['duration'], [], 'duration', 'Access Duration', 'Time', label_col = 'access number')

def revisit_diagram_graphical_interval_pie_graph(stk_obj : StkAccess, start_time=None, stop_time=None):
    root = stk_obj.base.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    
    df = stk_obj.data_providers.item('Access Data').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Revisit Diagram', 'Time')

def access_cumulative_dwell_graphical_cumulative_pie_graph(stk_obj : StkAccess, start_time=None, stop_time=None):
    root = stk_obj.base.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    
    df = stk_obj.data_providers.item('Access Data').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Cumulative Dwell', 'Time', True)