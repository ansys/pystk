from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def access_durations_xy_graph(stk_obj : CoverageDefinition):
	"""A plot of the cumulative distribution of the access durations of all grid points. For each grid point, access intervals to each assigned asset are combined to determine the time intervals over which at least one asset has access to the grid point. The durations of these intervals, for all grid points, are then sorted from smallest to largest and the percentages are then plotted.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\CoverageDefinition\Access Duration.rsg.
	"""
	root = stk_obj.root
	df = stk_obj.data_providers.item('Access Duration').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
			{'y_name':'percent under', 'label':'% Under', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'},
			{'y_name':'percent over', 'label':'% Over', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
	return line_chart(df, root, ['percent under','percent over'], ['duration'], axes, 'duration','Duration', 'Access Durations' )

def coverage_by_latitude_xy_graph(stk_obj : CoverageDefinition):
	"""A plot of the percent time covered vs latitude. A point is considered to be covered if it has access to one or more of the assigned assets. The reported values for each latitude are the average value for all grid points at that latitude.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\CoverageDefinition\Coverage By Latitude.rsg.
	"""
	root = stk_obj.root
	df = stk_obj.data_providers.item('Coverage by Latitude').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
			{'y_name':'percent time covered', 'label':'% Time Covered', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
	return line_chart(df, root, ['latitude','percent time covered'], [], axes, 'latitude','Latitude', 'Coverage By Latitude' )

def gap_durations_xy_graph(stk_obj : CoverageDefinition):
	"""A plot of the cumulative distribution of the access duration gaps of all grid points. For each grid point, access intervals to each assigned asset are combined to determine the time intervals over which at least one asset has access to the grid point. The durations of the gaps between these intervals, for all grid points, are then sorted from smallest to largest and the percentages are then plotted.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\CoverageDefinition\Gap Duration.rsg.
	"""
	root = stk_obj.root
	df = stk_obj.data_providers.item('Coverage Gap Duration').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
			{'y_name':'percent under', 'label':'% Under', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'},
			{'y_name':'percent over', 'label':'% Over', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
	return line_chart(df, root, ['percent under','percent over'], ['duration'], axes, 'duration','Duration', 'Gap Durations' )

def point_coverage_intervals_interval_graph(stk_obj :CoverageDefinition, start_time=None, stop_time=None):
	"""An Interval graph of the access intervals for the point currently selected by the grid inspector. The intervals represent the union of times that the grid point has access to any of the assets.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\CoverageDefinition\GI Point Coverage.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Selected Point Coverage').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('access start', 'None'),('access end', 'None'))]
	return interval_plot([df], elements, [], ['access start','access end'], 'Time', 'Point Coverage Intervals')

def probability_of_coverage_xy_graph(stk_obj : CoverageDefinition):
	"""A plot of the probability of coverage being achieved for the point selected in the grid inspector, as a function of the time past a request for coverage. 

	This graph wrapper was generated from AGI\STK12\STKData\Styles\CoverageDefinition\GI Point Prob Of Coverage.rsg.
	"""
	root = stk_obj.root
	df = stk_obj.data_providers.item('Selected Point Probability of Coverage').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
			{'y_name':'probability of collection', 'label':'Probability of Collection', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
	return line_chart(df, root, ['probability of collection'], ['time from request'], axes, 'time from request','Time From Request', 'Probability of Coverage' )

def percentage_of_region_covered_time_xy_graph(stk_obj :CoverageDefinition, start_time=None, stop_time=None, step=60):
	"""A plot of the percentage of coverage over time of the region selected by the grid inspector. A region is considered to be covered if at least one point within the region has access to one or more of the assigned assets.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\CoverageDefinition\GI Region Coverage.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Selected Region Coverage').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
			{'y_name':'percent coverage', 'label':'% Coverage', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
	return line_chart_time_x(df, root, ['percent coverage'], ['time'], axes, 'Percentage of Region Covered')

def intervals_of_full_regional_coverage_interval_graph(stk_obj :CoverageDefinition, start_time=None, stop_time=None):
	"""An Interval graph of the intervals of time when the region selected by the grid inspector is completely covered. The region is considered to be completely covered when all points within the region are covered. A point is covered when it has access to some asset.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\CoverageDefinition\GI Region Full Coverage.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Selected Region Full Coverage').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('coverage start', 'None'),('coverage end', 'None'))]
	return interval_plot([df], elements, [], ['coverage start','coverage end'], 'Time', 'Intervals of Full Regional Coverage')

def gi_region_time_to_cover_time_xy_graph(stk_obj :CoverageDefinition, start_time=None, stop_time=None, step=60):
	"""A plot of the amount of wait time required, starting from the reported time, before complete coverage of the region selected in the grid inspector occurs. The average wait time, compute as the mean of samples, is also plotted. A region is considered to be completely covered if all points within the region have had access to at least one of the assigned assets.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\CoverageDefinition\GI Region Time to Cover.rsg.
	"""
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
	"""A plot of the percentage of the area of the total coverage grid which is covered at the reported time.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\CoverageDefinition\Percent Coverage.rsg.
	"""
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

