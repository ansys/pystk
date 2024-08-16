"""Provides graphs for Radar objects."""
from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def antenna_gain_xy_graph(stk_obj : Radar):
    r"""Graph provides the detailed information for an antenna gain pattern. Each point on the graph conforms to a direction angle from the center of the antenna (phase center) through the gain pattern, with a user-specified angle step. The graph shows antenna gain value as a function of elevation angle and azimuth angle.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Radar\Antenna Gain.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Antenna Gain').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'gain', 'label':'Gain', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
    return line_chart(df, root, ['elevation','gain'], [], axes, 'elevation','Elevation', 'Antenna Gain' )

def antgain_azi_cut_vs_elevation_xy_graph(stk_obj : Radar):
    r"""Is set of graphs where each individual graph provides the antenna gain for a given azimuth angle across a specified range of elevation angles.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Radar\AntGain Azi Cut Vs Elevation.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Antenna Gain').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'gain', 'label':'Gain', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
    return line_chart(df, root, ['elevation','gain'], [], axes, 'elevation','Elevation', 'AntGain Azi Cut Vs Elevation' )

def antgain_elev_cut_vs_azimuth_xy_graph(stk_obj : Radar):
    r"""Is set of graphs where each individual graph provides the antenna gain for a given elevation angle across a specified range of azimuth angles.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Radar\AntGain Elev Cut Vs Azimuth.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Antenna Gain').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'gain', 'label':'Gain', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
    return line_chart(df, root, ['azimuth','gain'], [], axes, 'azimuth','Azimuth', 'AntGain Elev Cut Vs Azimuth' )

