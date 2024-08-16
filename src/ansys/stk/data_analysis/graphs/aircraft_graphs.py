from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def cumulative_sunlight_cumulative_pie_graph(stk_obj :Aircraft, start_time=None, stop_time=None):
	"""A Pie chart showing the total duration of full sunlight within the graph's requested time interval. Gaps in the chart indicate the total duration of penumbra and umbra durations.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Cumulative Sunlight.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Lighting Times').group.item('Sunlight').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Cumulative Sunlight', 'Time', True)

def eclipse_times_interval_graph(stk_obj :Aircraft, start_time=None, stop_time=None):
	"""An Interval graph of the penumbra (partial lighting) and umbra (zero lighting) intervals.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Eclipse Times.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Eclipse Times').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('start time', 'None'),('stop time', 'None'))]
	return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Eclipse Times')

def flight_profile_by_down_range_xy_graph(stk_obj : Aircraft):
	"""A plot of altitude and true air speeed as a function of downrange distance. 

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Flight Profile by DownRange.rsg.
	"""
	root = stk_obj.root
	df = stk_obj.data_providers.item('Flight Profile By Down Range').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': ' Altitude', 'lines': [
			{'y_name':'altitude-msl', 'label':'Altitude-MSL', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'AviatorAltitude'}]},
			{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': ' Speed', 'lines': [
			{'y_name':'tas', 'label':'TAS', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'AviatorSpeed'}]}]
	return line_chart(df, root, ['downrange','altitude-msl','tas'], [], axes, 'downrange','Down Range', 'Flight Profile By Down Range' )

def flight_profile_by_time_time_xy_graph(stk_obj :Aircraft, start_time=None, stop_time=None, step=60):
	"""A plot of altitude and true air speeed as a function of time. 

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Flight Profile by Time.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Flight Profile By Time').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': ' Altitude', 'lines': [
			{'y_name':'altitude-msl', 'label':'Altitude-MSL', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'AviatorAltitude'}]},
			{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': ' Speed', 'lines': [
			{'y_name':'tas', 'label':'TAS', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'AviatorSpeed'}]}]
	return line_chart_time_x(df, root, ['altitude-msl','tas'], ['time'], axes, 'Flight Profile By Time')

def lasercat_clear_firing_interval_graph(stk_obj :Aircraft, start_time=None, stop_time=None):
	"""An Interval graph of the time intervals in which the object can communicate with the target without any unintended lasing of other satellites, as computed by the LaserCAT tool.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\LaserCATClearFiring.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('LaserCAT Clear Firing').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('start clear', 'None'),('stop clear', 'None'))]
	return interval_plot([df], elements, [], ['start clear','stop clear'], 'Time', 'LaserCAT Clear Firing')

def lasercat_potential_victim_interval_graph(stk_obj :Aircraft, start_time=None, stop_time=None):
	"""An Interval graph of the time intervals during which potential victims (i) may interfere with the communication link or (ii) be subject to interference from the communications link, as computed by the LaserCAT tool. These intervals occur during times when the object can communicate with the target.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\LaserCATPotentialVictim.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('LaserCAT Potential Victim').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('time in', 'None'),('time out', 'None'))]
	return interval_plot([df], elements, [], ['time in','time out'], 'Time', 'LaserCAT Potential Victim')

def lighting_times_interval_graph(stk_obj :Aircraft, start_time=None, stop_time=None):
	"""An Interval graph of the sunlight (full lighting) intervals, penumbra (partial lighting) intervals and umbra (zero lighting) intervals. Each lighting condition's intervals are plotted on separate lines.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Lighting Times.rsg.
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

def lla_position_time_xy_graph(stk_obj :Aircraft, start_time=None, stop_time=None, step=60):
	"""The position of the object, expressed in LLA elements, as a function of time. The coordinate system is the Fixed frame of the object's central body.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\LLA Position.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('LLA State').group.item('Fixed').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Latitude/Longitude', 'lines': [
			{'y_name':'lat', 'label':'Lat', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Latitude'},
			{'y_name':'lon', 'label':'Lon', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Longitude'}]},
			{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
			{'y_name':'alt', 'label':'Alt', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]}]
	return line_chart_time_x(df, root, ['lat','lon','alt'], ['time'], axes, 'LLA Position')

def model_area_time_xy_graph(stk_obj :Aircraft, start_time=None, stop_time=None, step=60):
	"""A plot of the area of the object's 3D graphics model over time, as viewed from a given view direction, as computed by the Area Tool.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Model Area.rsg.
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

def rfi_potential_victim_interval_graph(stk_obj :Aircraft, start_time=None, stop_time=None):
	"""An Interval graph of the time intervals during which potential victims (i) may interfere with the communication link or (ii) be subject to interference from the communications link, as computed by the Radio Frequency Interference (RFI) Analysis tool. These intervals occur during times when the object can communicate with the target.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\RFIPotentialVictim.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('RFI Potential Victim').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	elements=[(('time in', 'None'),('time out', 'None'))]
	return interval_plot([df], elements, [], ['time in','time out'], 'Time', 'RFI Potential Victim')

def ecf_vvlh_solar_aer_time_xy_graph(stk_obj :Aircraft, start_time=None, stop_time=None, step=60):
	"""A plot of the azimuth, elevation, and range over time, describing the apparent relative position vector of the Sun with respect to Fixed VVLH axes (ECFVVLH).

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Solar AER.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Lighting AER').group.item('ECFVVLH').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
			{'y_name':'azimuth', 'label':'Azimuth', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'},
			{'y_name':'elevation', 'label':'Elevation', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]},
			{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
			{'y_name':'range', 'label':'Range', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]}]
	return line_chart_time_x(df, root, ['azimuth','elevation','range'], ['time'], axes, 'ECF VVLH Solar AER')

def solar_ecf_vvlh_az_el_polar_center_0_graph(stk_obj :Aircraft, start_time=None, stop_time=None, step=60):
	"""A polar plot with elevation as radius and azimuth as angle theta over time, describing the apparent relative position vector of the Sun with respect to Fixed VVLH axes (ECFVVLH).

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Solar Az-El.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Lighting AER').group.item('ECFVVLH').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axis={'use_unit' : True, 'unit_squared': False, 'label': 'Angle', 'lines': [
		{'y_name':'elevation','x_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': False, 'unit_pref': 'Angle'}
		]}
	return polar_chart(df, root, ['elevation','azimuth'], axis, 'Solar ECF VVLH Az-El', convert_negative_r = True, origin_0 = True )

def solar_intensity_time_xy_graph(stk_obj :Aircraft, start_time=None, stop_time=None, step=60):
	"""A plot of the percent of the solar disc visible over time.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Solar Intensity.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Solar Intensity').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
			{'y_name':'intensity', 'label':'Intensity', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
	return line_chart_time_x(df, root, ['intensity'], ['time'], axes, 'Solar Intensity')

def area_time_xy_graph(stk_obj :Aircraft, start_time=None, stop_time=None, step=60):
	"""A plot of the effective area of the solar panels illuminated by the sun over time.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Solar Panel Area.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Solar Panel Area').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': True, 'ylog10': False, 'y2log10': False, 'label': ' Area', 'lines': [
			{'y_name':'effective area', 'label':'Effective Area', 'use_unit':None, 'unit_squared': True, 'unit_pref': 'SmallDistance'}]}]
	return line_chart_time_x(df, root, ['effective area'], ['time'], axes, 'Area')

def power_time_xy_graph(stk_obj :Aircraft, start_time=None, stop_time=None, step=60):
	"""A plot of the power of the solar panels illuminated by the sun over time.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Solar Panel Power.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Solar Panel Power').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Power', 'lines': [
			{'y_name':'power', 'label':'Power', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Power'}]}]
	return line_chart_time_x(df, root, ['power'], ['time'], axes, 'Power')

def sun_vector_ecf_time_xy_graph(stk_obj :Aircraft, start_time=None, stop_time=None, step=60):
	"""A plot of the apparent relative position of the Sun to the object, expressed in Cartesian components, using the object's central body's Fixed coordinate system, as a function of time. 

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Sun Vector ECF.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Sun Vector').group.item('Fixed').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
			{'y_name':'x', 'label':'x', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'},
			{'y_name':'y', 'label':'y', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'},
			{'y_name':'z', 'label':'z', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]}]
	return line_chart_time_x(df, root, ['x','y','z'], ['time'], axes, 'Sun Vector ECF')

def sunlight_intervals_interval_pie_graph(stk_obj :Aircraft, start_time=None, stop_time=None):
	"""A Pie chart showing each interval of full sunlight within the graph's requested time interval, separated by gaps indicating the intervals of penumbra/umbra lighting condition before and after each sunlight interval.

	This graph wrapper was generated from AGI\STK12\STKData\Styles\Aircraft\Sunlight Intervals.rsg.
	"""
	root = stk_obj.root
	if start_time is None:
		start_time = root.current_scenario.start_time
	if stop_time is None:
		stop_time = root.current_scenario.stop_time
	df = stk_obj.data_providers.item('Lighting Times').group.item('Sunlight').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
	return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Sunlight Intervals', 'Time')

