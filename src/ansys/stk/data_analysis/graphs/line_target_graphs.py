from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def anchor_point_solar_az_el_time_xy_graph(stk_obj :LineTarget, start_time=None, stop_time=None, step=60):
	"""A plot of the elevation and azimuth over time, describing the relative position vector of the apparent Sun to the anchor point, with respect to the local horizontal plane. This frame has the Z axis aligned with the inward surface normal direction (minus Z is up) and the X axis constrained toward the local north direction.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\LineTarget\Anchor Point Solar Az-El.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Anchor Point Lighting AER').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
			{'y_name':'azimuth', 'label':'Azimuth', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Longitude'},
			{'y_name':'elevation', 'label':'Elevation', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]}]
	return line_chart_time_x(df, root, ['azimuth','elevation'], ['time'], axes, 'Anchor Point Solar Az-El')

