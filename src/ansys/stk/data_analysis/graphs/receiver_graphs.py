"""Provides graphs for Receiver objects."""
from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def antgain_azi_cut_vs_elevation_xy_graph(stk_obj : Receiver):
    r"""Is set of graphs where each individual graph provides the antenna gain for a given azimuth angle across a specified range of elevation angles.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Receiver\AntGain Azi Cut Vs Elevation.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Antenna Gain').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'gain', 'label':'Gain', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
    return line_chart(df, root, ['elevation','gain'], [], axes, 'elevation','Elevation', 'AntGain Azi Cut Vs Elevation' )

def antgain_elev_cut_vs_azimuth_xy_graph(stk_obj : Receiver):
    r"""Is set of graphs where each individual graph provides the antenna gain for a given elevation angle across a specified range of azimuth angles.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Receiver\AntGain Elev Cut Vs Azimuth.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Antenna Gain').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'gain', 'label':'Gain', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
    return line_chart(df, root, ['azimuth','gain'], [], axes, 'azimuth','Azimuth', 'AntGain Elev Cut Vs Azimuth' )

def receiver_filter_xy_graph(stk_obj : Receiver):
    r"""Show the receiver RF filter magnitude data as a function of receiver bandwidth frequency.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Receiver\Receiver Filter.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Receiver Filter').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'filtermagnitude', 'label':'FilterMagnitude', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
    return line_chart(df, root, ['bandfrequency','filtermagnitude'], [], axes, 'bandfrequency','Band Frequency', 'Receiver Filter' )

