from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def antgain_azi_cut_vs_elevation_xy_graph(stk_obj : Transmitter):
	"""This is set of graphs where each individual graph provides the antenna gain for a given azimuth angle across a specified range of elevation angles."""
	root = stk_obj.root
	df = stk_obj.data_providers.item('Antenna Gain').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
			{'y_name':'gain', 'label':'Gain', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
	return line_chart(df, root, ['elevation','gain'], [], axes, 'elevation','Elevation', 'AntGain Azi Cut Vs Elevation' )

def antgain_elev_cut_vs_azimuth_xy_graph(stk_obj : Transmitter):
	"""This is set of graphs where each individual graph provides the antenna gain for a given elevation angle across a specified range of azimuth angles."""
	root = stk_obj.root
	df = stk_obj.data_providers.item('Antenna Gain').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
			{'y_name':'gain', 'label':'Gain', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
	return line_chart(df, root, ['azimuth','gain'], [], axes, 'azimuth','Azimuth', 'AntGain Elev Cut Vs Azimuth' )

def transmitter_spectrum_and_filter_xy_graph(stk_obj : Transmitter):
	"""This report shows the spectrum of a modulated RF signal as a function of the frequency across the RF bandwidth of a transmitter. It also lists the profile of the transmitter filter magnitude and the profile of the filtered spectrum as modified by the filter."""
	root = stk_obj.root
	df = stk_obj.data_providers.item('Transmitter Spectrum and Filter').exec().data_sets.to_pandas_dataframe()
	axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
			{'y_name':'spectrummagnitude', 'label':'SpectrumMagnitude', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'},
			{'y_name':'filtermagnitude', 'label':'FilterMagnitude', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'},
			{'y_name':'filteredspectrum', 'label':'FilteredSpectrum', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
	return line_chart(df, root, ['bandfrequency','spectrummagnitude','filtermagnitude','filteredspectrum'], [], axes, 'bandfrequency','Band Frequency', 'Transmitter Spectrum and Filter' )

