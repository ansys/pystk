from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def cumulative_sunlight_cumulative_pie_graph(stk_obj :Target, start_time=None, stop_time=None):
	"""A Pie chart showing the total duration of full sunlight within the graph's requested time interval. Gaps in the chart indicate the total duration of penumbra and umbra durations.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Target\Cumulative Sunlight.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Lighting Times').group.item('Sunlight').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Cumulative Sunlight', 'Time', True)

def eclipse_times_interval_graph(stk_obj :Target, start_time=None, stop_time=None):
	"""An Interval graph of the penumbra (partial lighting) and umbra (zero lighting) intervals.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Target\Eclipse Times.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Eclipse Times').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('start time', 'None'),('stop time', 'None'))]
	return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Eclipse Times')

def lighting_times_interval_graph(stk_obj :Target, start_time=None, stop_time=None):
	"""An Interval graph of the sunlight (full lighting) intervals, penumbra (partial lighting) intervals and umbra (zero lighting) intervals. Each lighting condition's intervals are plotted on separate lines.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Target\Lighting Times.rsg.
	"""
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

def model_area_time_xy_graph(stk_obj :Target, start_time=None, stop_time=None, step=60):
	"""A plot of the area of the object's 3D graphics model over time, as viewed from a given view direction, as computed by the Area Tool.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Target\Model Area.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Model Area').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Area', 'lines': [
			{'y_name':'area', 'label':'Area', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Area'}]}]
	return line_chart_time_x(df, root, ['area'], ['time'], axes, 'Model Area')

def solar_aer_time_xy_graph(stk_obj :Target, start_time=None, stop_time=None, step=60):
	"""A plot of the azimuth, elevation, and range over time, describing the apparent relative position vector of the Sun with respect to the local horizontal plane.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Target\Solar AER.rsg.
	"""
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

def solar_az_el_polar_center_0_graph(stk_obj :Target, start_time=None, stop_time=None, step=60):
	"""A polar plot with elevation as radius and azimuth as angle theta over time, describing the apparent relative position vector of the Sun with respect to the local horizontal plane.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Target\Solar Az-El.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Lighting AER').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axis={'use_unit' : True, 'unit_squared': False, 'label': 'Angle', 'lines': [
		{'y_name':'elevation','x_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': False, 'unit_pref': 'Angle'}
		]}
	return polar_chart(df, root, ['elevation','azimuth'], axis, 'Solar Az-El', convert_negative_r = True, origin_0 = True )

def sunlight_intervals_interval_pie_graph(stk_obj :Target, start_time=None, stop_time=None):
	"""A Pie chart showing each interval of full sunlight within the graph's requested time interval, separated by gaps indicating the intervals of penumbra/umbra lighting condition before and after each sunlight interval.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Target\Sunlight Intervals.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Lighting Times').group.item('Sunlight').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Sunlight Intervals', 'Time')

