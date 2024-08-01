from graph_functions import *
from ansys.stk.core.stkobjects import *

def percent_sunlight_cumulative_pie_graph(stk_obj :Facility, start_time=None, stop_time=None):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Lighting Times').group.item('Sunlight').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Percent Sunlight', 'Time', True)

def eclipse_times_interval_graph(stk_obj :Facility, start_time=None, stop_time=None):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Eclipse Times').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('start time', '0'),('stop time', '0'))]
	return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Eclipse Times')

def lasercat_clear_firing_interval_graph(stk_obj :Facility, start_time=None, stop_time=None):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('LaserCAT Clear Firing').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('start clear', '0'),('stop clear', '0'))]
	return interval_plot([df], elements, [], ['start clear','stop clear'], 'Time', 'LaserCAT Clear Firing')

def lasercat_potential_victim_interval_graph(stk_obj :Facility, start_time=None, stop_time=None):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('LaserCAT Potential Victim').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('time in', '0'),('time out', '0'))]
	return interval_plot([df], elements, [], ['time in','time out'], 'Time', 'LaserCAT Potential Victim')

def lighting_times_interval_graph(stk_obj :Facility, start_time=None, stop_time=None):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df_list=[]
	df_list.append(stk_obj.data_providers.item('Lighting Times').group.item('Sunlight').exec(start_time, stop_time).data_sets.to_pandas_dataframe())
	df_list.append(stk_obj.data_providers.item('Lighting Times').group.item('Penumbra').exec(start_time, stop_time).data_sets.to_pandas_dataframe())
	df_list.append(stk_obj.data_providers.item('Lighting Times').group.item('Umbra').exec(start_time, stop_time).data_sets.to_pandas_dataframe())
	elements=[(('start time', 'Sunlight'),('stop time', 'Sunlight')),(('start time', 'Penumbra'),('stop time', 'Penumbra')),(('start time', 'Umbra'),('stop time', 'Umbra'))]
	return interval_plot(df_list, elements, [], ['start time','stop time'], 'Time', 'Lighting Times')

def model_area_time_xy_graph(stk_obj :Facility, start_time=None, stop_time=None, step=60):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Model Area').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Area', 'lines': [
			{'y_name':'area', 'label':'Area', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Area'}]}]
	return line_chart_time_x(df, root, ['area'], ['time'], axes, 'Model Area')

def rfi_potential_victim_interval_graph(stk_obj :Facility, start_time=None, stop_time=None):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('RFI Potential Victim').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('time in', '0'),('time out', '0'))]
	return interval_plot([df], elements, [], ['time in','time out'], 'Time', 'RFI Potential Victim')

def solar_aer_time_xy_graph(stk_obj :Facility, start_time=None, stop_time=None, step=60):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Lighting AER').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
			{'y_name':'azimuth', 'label':'Azimuth', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'},
			{'y_name':'elevation', 'label':'Elevation', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]},
			{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
			{'y_name':'range', 'label':'Range', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]}]
	return line_chart_time_x(df, root, ['azimuth','elevation','range'], ['time'], axes, 'Solar AER')

def solar_az_el_polar_center_0_graph(stk_obj :Facility, start_time=None, stop_time=None, step=60):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Lighting AER').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axis={'use_unit' : True, 'unit_squared': False, 'label': 'Angle', 'lines': [
		{'y_name':'elevation','x_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': False, 'unit_pref': 'Angle'}]}
	return polar_chart(df, root, ['elevation','azimuth'], axis, 'Solar Az-El', origin_0 = True, convert_negative_r = True)

def sunlight_intervals_interval_pie_graph(stk_obj :Facility, start_time=None, stop_time=None):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Lighting Times').group.item('Sunlight').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Sunlight Intervals', 'Time')