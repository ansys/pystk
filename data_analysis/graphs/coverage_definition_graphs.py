from graph_functions import *
from ansys.stk.core.stkobjects import *

def access_durations_xy_graph(stk_obj : CoverageDefinition):
	root = stk_obj.root
	df = stk_obj.data_providers.item('Access Duration').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
			{'y_name':'percent under', 'label':'% Under', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'},
			{'y_name':'percent over', 'label':'% Over', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
	return line_chart(df, root, ['percent under','percent over'], ['duration'], axes, 'duration','Duration', 'Access Durations')

def coverage_by_latitude_xy_graph(stk_obj : CoverageDefinition):
	root = stk_obj.root
	df = stk_obj.data_providers.item('Coverage by Latitude').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
			{'y_name':'percent time covered', 'label':'% Time Covered', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
	return line_chart(df, root, ['latitude','percent time covered'], [], axes, 'latitude','Latitude', 'Coverage By Latitude')

def gap_durations_xy_graph(stk_obj : CoverageDefinition):
	root = stk_obj.root
	df = stk_obj.data_providers.item('Coverage Gap Duration').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
			{'y_name':'percent under', 'label':'% Under', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'},
			{'y_name':'percent over', 'label':'% Over', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
	return line_chart(df, root, ['percent under','percent over'], ['duration'], axes, 'duration','Duration', 'Gap Durations')

def point_coverage_intervals_interval_graph(stk_obj :CoverageDefinition, start_time=None, stop_time=None):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Selected Point Coverage').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('access start', '0'),('access end', '0'))]
	return interval_plot([df], elements, [], ['access start','access end'], 'Time', 'Point Coverage Intervals')

def probability_of_coverage_xy_graph(stk_obj : CoverageDefinition):
	root = stk_obj.root
	df = stk_obj.data_providers.item('Selected Point Probability of Coverage').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
			{'y_name':'probability of collection', 'label':'Probability of Collection', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
	return line_chart(df, root, ['probability of collection'], ['time from request'], axes, 'time from request','Time From Request', 'Probability of Coverage')

def percentage_of_region_covered_time_xy_graph(stk_obj :CoverageDefinition, start_time=None, stop_time=None, step=60):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Percent Coverage').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
			{'y_name':'percent coverage', 'label':'% Coverage', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
	return line_chart_time_x(df, root, ['percent coverage'], ['time'], axes, 'Percentage of Region Covered')

def intervals_of_full_regional_coverage_interval_graph(stk_obj :CoverageDefinition, start_time=None, stop_time=None):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Selected Region Full Coverage').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('coverage start', '0'),('coverage end', '0'))]
	return interval_plot([df], elements, [], ['coverage start','coverage end'], 'Time', 'Intervals of Full Regional Coverage')

def gi_region_time_to_cover_time_xy_graph(stk_obj :CoverageDefinition, start_time=None, stop_time=None, step=60):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Selected Region Time To Cover').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Time', 'lines': [
			{'y_name':'wait for total cov', 'label':'Wait for Total Cov', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Time'},
			{'y_name':'average sampled wait', 'label':'Average Sampled Wait', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Time'}]}]
	return line_chart_time_x(df, root, ['wait for total cov','average sampled wait'], ['time'], axes, 'GI Region Time to Cover')

def current_and_accumulated_coverage_time_xy_graph(stk_obj :CoverageDefinition, start_time=None, stop_time=None, step=60):
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Percent Coverage').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
			{'y_name':'percent coverage', 'label':'% Coverage', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'},
			{'y_name':'percent accum coverage', 'label':'% Accum Coverage', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
	return line_chart_time_x(df, root, ['percent coverage','percent accum coverage'], ['time'], axes, 'Current and Accumulated Coverage')