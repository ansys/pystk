from graph_functions import *
from ansys.stk.core.stkobjects import *

def access_duration_pie_graph(stk_obj :StkAccess, start_time=None, stop_time=None):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Access Data').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	return pie_chart(root, df, ['duration'], [], 'duration', 'Access Duration', 'Time', 'access number')

def access_times_interval_graph(stk_obj :StkAccess, start_time=None, stop_time=None):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Access Data').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('start time', '0'),('stop time', '0'))]
	return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Access Times')

def aer_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
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
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('AER Data').group.item('Default').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axis={'use_unit' : True, 'unit_squared': False, 'label': 'Angle', 'lines': [
		{'y_name':'elevation','x_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': False, 'unit_pref': 'Angle'}]}
	return polar_chart(df, root, ['elevation','azimuth'], axis, 'Az El Polar', convert_negative_r = False, origin_0 = False ,groupby='access number' )

def bit_error_rate_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
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
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Access Data').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Cumulative Dwell', 'Time', True)

def ebno_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
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
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Access Gaps').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('start time', '0'),('stop time', '0'))]
	return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Access Gap Periods')

def probability_of_detection_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
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

def radar_rcs_detailed_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar RCS').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Radar Cross Section', 'lines': [
			{'y_name':'rcs', 'label':'RCS', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'RadarCrossSection'}]},
			{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
			{'y_name':'bodyfixed az', 'label':'BodyFixed Az', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'},
			{'y_name':'bodyfixed el', 'label':'BodyFixed El', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]}]
	return line_chart_time_x(df, root, ['rcs','bodyfixed az','bodyfixed el'], ['time'], axes, 'Radar RCS - Detailed')

def radar_rcs_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar RCS').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Radar Cross Section', 'lines': [
			{'y_name':'rcs', 'label':'RCS', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'RadarCrossSection'}]}]
	return line_chart_time_x(df, root, ['rcs'], ['time'], axes, 'Radar RCS')

def radar_sar_azimuth_resolution_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar SAR').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
			{'y_name':'sar az resolution', 'label':'SAR Az Resolution', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]},
			{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Time', 'lines': [
			{'y_name':'sar integration time', 'label':'SAR Integration Time', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Time'}]}]
	return line_chart_time_x(df, root, ['sar az resolution','sar integration time'], ['time'], axes, 'Radar SAR Azimuth Resolution')

def radar_sar_time_resolution_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar SAR').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Sar Time Res Prod', 'lines': [
			{'y_name':'sar time-resolution prod', 'label':'SAR Time-Resolution Prod', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'SarTimeResProd'}]}]
	return line_chart_time_x(df, root, ['sar time-resolution prod'], ['time'], axes, 'Radar SAR Time-Resolution')

def radar_searchtrack_integration_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar SearchTrack').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': ' Time', 'lines': [
			{'y_name':'s/t integration time', 'label':'S/T Integration Time', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'SmallTime'},
			{'y_name':'s/t dwell time', 'label':'S/T Dwell Time', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'SmallTime'}]},
			{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
			{'y_name':'s/t pulses integrated', 'label':'S/T Pulses Integrated', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
	return line_chart_time_x(df, root, ['s/t integration time','s/t dwell time','s/t pulses integrated'], ['time'], axes, 'Radar SearchTrack Integration')

def radar_searchtrack_snr_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar SearchTrack').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
			{'y_name':'s/t snr1', 'label':'S/T SNR1', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
	return line_chart_time_x(df, root, ['s/t snr1'], ['time'], axes, 'Radar SearchTrack SNR')

def radar_skywave_dopplers_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar Environment - VOACAP').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Frequency', 'lines': [
			{'y_name':'skywave doppler-primaryprimary (xm-sky-tgt-sky-rc)', 'label':'Skywave Doppler-PrimaryPrimary (Xm-Sky-Tgt-Sky-Rc)', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Frequency'},
			{'y_name':'skywave doppler-primarysecondary (xm-sky-tgt-gndsky-rc)', 'label':'Skywave Doppler-PrimarySecondary (Xm-Sky-Tgt-GndSky-Rc)', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Frequency'},
			{'y_name':'skywave doppler-secondaryprimary (xm-skygnd-tgt-sky-rc)', 'label':'Skywave Doppler-SecondaryPrimary (Xm-SkyGnd-Tgt-Sky-Rc)', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Frequency'},
			{'y_name':'skywave doppler-secondarysecondary (xm-skygnd-tgt-gndsky-rc)', 'label':'Skywave Doppler-SecondarySecondary (Xm-SkyGnd-Tgt-GndSky-Rc)', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Frequency'}]}]
	return line_chart_time_x(df, root, ['skywave doppler-primaryprimary (xm-sky-tgt-sky-rc)','skywave doppler-primarysecondary (xm-sky-tgt-gndsky-rc)','skywave doppler-secondaryprimary (xm-skygnd-tgt-sky-rc)','skywave doppler-secondarysecondary (xm-skygnd-tgt-gndsky-rc)'], ['time'], axes, 'Radar Skywave Dopplers')

def radar_system_noise_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar Environment').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Temperature', 'lines': [
			{'y_name':'antenna temp', 'label':'Antenna Temp', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Temperature'},
			{'y_name':'system temp', 'label':'System Temp', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Temperature'}]}]
	return line_chart_time_x(df, root, ['antenna temp','system temp'], ['time'], axes, 'Radar System Noise')

def revisit_diagram_interval_pie_graph(stk_obj :StkAccess, start_time=None, stop_time=None):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Access Data').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Revisit Diagram', 'Time')

def signal_to_noise_ratio_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Radar SearchTrack').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
			{'y_name':'s/t snr1', 'label':'S/T SNR1', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
	return line_chart_time_x(df, root, ['s/t snr1'], ['time'], axes, 'Signal to Noise Ratio')

def sun_rfi_time_xy_graph(stk_obj :StkAccess, start_time=None, stop_time=None, step=60):
	root = stk_obj.base.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Link Information').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Temperature', 'lines': [
			{'y_name':'tsun', 'label':'Tsun', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Temperature'}]},
			{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
			{'y_name':'g/t (db/k)', 'label':'g/T (dB/K)', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
	return line_chart_time_x(df, root, ['tsun','g/t (db/k)'], ['time'], axes, 'Sun RFI')

