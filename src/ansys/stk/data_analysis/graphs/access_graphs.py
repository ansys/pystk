from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def access_duration_pie_graph(stk_obj :StkAccess, start_time=None, stop_time=None):
	"""A pie chart of the durations of the access intervals."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Access Data').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	return pie_chart(root, df, ['duration'], [], 'duration', 'Access Duration', 'Time', 'access number')

def access_times_interval_graph(stk_obj :StkAccess, start_time=None, stop_time=None):
	"""An Interval graph of the access intervals."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Access Data').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('start time', '0'),('stop time', '0'))]
	return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Access Times')

def aer_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	"""A plot of the azimuth, elevation, and range values for the relative position vector between the base object and the target object, during access intervals. The relative position includes the effects of light time delay and aberration as set by the computational settings of the access. Az-El values are computed with respect to the default AER frame of the selected object of the Access Tool, as described below. """
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('AER Data').group.item('Default').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Longitude/Angle', 'lines': [
			{'y_name':'azimuth', 'label':'Azimuth', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Longitude'},
			{'y_name':'elevation', 'label':'Elevation', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]},
			{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
			{'y_name':'range', 'label':'Range', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]}]
	return line_chart_time_x(df, root, ['azimuth','elevation','range'], ['time'], axes, 'AER', groupby='access number')

def angular_rates_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	"""A plot of the azimuth rate, elevation rate, and angular rate over time, during each access interval, from the perspective of the selected object in the Access Tool. The azimuth rate, elevation rate, and angular rate are available only if the selected object supports that metric as an access constraint: the value being reported is that as computed by that access constraint."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Constraint Data').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle Rate', 'lines': [
			{'y_name':'fromangularrate', 'label':'FromAngularRate', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'AngleRate'},
			{'y_name':'fromazimuthrate', 'label':'FromAzimuthRate', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'AngleRate'},
			{'y_name':'fromelevationrate', 'label':'FromElevationRate', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'AngleRate'}]}]
	return line_chart_time_x(df, root, ['fromangularrate','fromazimuthrate','fromelevationrate'], ['time'], axes, 'Angular Rates')

def az_el_polar_polar_center_90_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	"""A polar plot with elevation as radius and azimuth as angle theta over time, during access intervals. The azimuth and elevation describe the relative position vector between the base object and the target object. The relative position includes the effects of light time delay and aberration as set by the computational settings of the access. Az-El values are computed with respect to the default AER frame of the selected object of the Access Tool, as described below."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('AER Data').group.item('0').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axis={'use_unit' : True, 'unit_squared': False, 'label': 'Angle', 'lines': [
		{'y_name':'elevation','x_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': False, 'unit_pref': 'Angle'}
		]}
	return polar_chart(df, root, ['elevation','azimuth'], axis, 'Az El Polar', convert_negative_r = False, origin_0 = False ,groupby='access number' )

def bit_error_rate_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	"""Plots the bit error rate (BER) over time, during each access interval."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Link Information').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
			{'y_name':'ber', 'label':'BER', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
	return line_chart_time_x(df, root, ['ber'], ['time'], axes, 'Bit Error Rate')

def carrier_to_noise_ratio_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	"""Plots the carrier to noise ratio (C/N) over time, during each access interval."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Link Information').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
			{'y_name':'c/n', 'label':'C/N', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
	return line_chart_time_x(df, root, ['c/n'], ['time'], axes, 'Carrier to Noise Ratio')

def cumulative_dwell_cumulative_pie_graph(stk_obj :StkAccess, start_time=None, stop_time=None):
	"""This graph shows access interval durations as a cumulative pie chart."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Access Data').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Cumulative Dwell', 'Time', True)

def ebno_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	"""Plots the energy per bit to noise ratio (Eb/No) over time, during each access interval."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Link Information').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
			{'y_name':'eb/no', 'label':'Eb/No', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
	return line_chart_time_x(df, root, ['eb/no'], ['time'], axes, 'EbNo')

def elevation_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	"""A plot of the elevation angle and its rate over time, during each access interval, from the perspective of the selected object in the Access Tool. The elevation angle value is that as computed by the elevation constraint for the selected object. The elevation rate is available only if the selected object supports that metric as an access constraint: the value being reported is that as computed by that access constraint."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Constraint Data').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
			{'y_name':'fromelevationangle', 'label':'FromElevationAngle', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]},
			{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle Rate', 'lines': [
			{'y_name':'fromelevationrate', 'label':'FromElevationRate', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'AngleRate'}]}]
	return line_chart_time_x(df, root, ['fromelevationangle','fromelevationrate'], ['time'], axes, 'Elevation')

def access_gap_periods_interval_graph(stk_obj :StkAccess, start_time=None, stop_time=None):
	"""An Interval graph of the intervals where access does not exist between the objects."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Access Gaps').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('start time', '0'),('stop time', '0'))]
	return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Access Gap Periods')

def probability_of_detection_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	"""This graph shows the probability of a radar pulse search detection versus time."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar SearchTrack').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
			{'y_name':'s/t pdet1', 'label':'S/T PDet1', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
	return line_chart_time_x(df, root, ['s/t pdet1'], ['time'], axes, 'Probability of Detection')

def radar_antenna_gain_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	"""This graph shows the antenna gain (value toward the Az, El direction)for both receiver and transmitter versus time."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar Antenna').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
			{'y_name':'rcvr ant gain', 'label':'Rcvr Ant Gain', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'},
			{'y_name':'xmtr ant gain', 'label':'Xmtr Ant Gain', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
	return line_chart_time_x(df, root, ['rcvr ant gain','xmtr ant gain'], ['time'], axes, 'Radar Antenna Gain')

def radar_propagation_loss_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	"""This graph shows the receive and transmit total propagation attenuation values for the primary polarization signal channel versus time."""
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar Environment').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
			{'y_name':'rcvr prop atten', 'label':'Rcvr Prop Atten', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'},
			{'y_name':'xmtr prop atten', 'label':'Xmtr Prop Atten', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
	return line_chart_time_x(df, root, ['rcvr prop atten','xmtr prop atten'], ['time'], axes, 'Radar Propagation Loss')

