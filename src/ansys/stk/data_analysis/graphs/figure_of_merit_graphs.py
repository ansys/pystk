"""Provides graphs for FigureOfMerit objects."""
from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def all_dilutions_of_precision_time_xy_graph(stk_obj :FigureOfMerit, start_time=None, stop_time=None, step=60):
    r"""Create plot of all DOP values, over time, for the point currently selected via the figure of merit grid inspector. 

    This graph wrapper was generated from AGI\STK12\STKData\Styles\FigureOfMerit\GI All DOP.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Selected Point All DOPs').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'gdop', 'label':'GDOP', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'pdop', 'label':'PDOP', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'hdop', 'label':'HDOP', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'vdop', 'label':'VDOP', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'edop', 'label':'EDOP', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'ndop', 'label':'NDOP', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'tdop', 'label':'TDOP', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
    return line_chart_time_x(df, root, ['gdop','pdop','hdop','vdop','edop','ndop','tdop'], ['time'], axes, 'All Dilutions of Precision')

def point_fom_value_time_xy_graph(stk_obj :FigureOfMerit, start_time=None, stop_time=None, step=60):
    r"""Create plot of the figure of merit values over time, for the point currently selected via the figure of merit grid inspector. 

    This graph wrapper was generated from AGI\STK12\STKData\Styles\FigureOfMerit\GI Point FOM.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Selected Point FOM').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'fom value', 'label':'FOM Value', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
    return line_chart_time_x(df, root, ['fom value'], ['time'], axes, 'Point FOM Value')

def point_satisfaction_intervals_interval_graph(stk_obj :FigureOfMerit, start_time=None, stop_time=None):
    r"""Createn Interval graph of the satisfaction intervals for the point currently selected via the figure of merit grid inspector. Satisfaction intervals are defined as periods when a grid point achieves the defined satisfaction criteria associated with the FOM. 

    This graph wrapper was generated from AGI\STK12\STKData\Styles\FigureOfMerit\GI Point Satisfaction.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Selected Point Satisfaction').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    elements=[(('interval start', 'None'),('interval end', 'None'))]
    return interval_plot([df], elements, [], ['interval start','interval end'], 'Time', 'Point Satisfaction Intervals')

def regional_fom_values_time_xy_graph(stk_obj :FigureOfMerit, start_time=None, stop_time=None, step=60):
    r"""Create plot of the minimum, maximum, and average figure of merit value, sampled over all grid points within the region currently selected in the figure of merit grid inspector, over time. Grid points for which a value cannot be computed are not included in the reported statistics. 

    This graph wrapper was generated from AGI\STK12\STKData\Styles\FigureOfMerit\GI Region FOM.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Selected Region FOM').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'minimum', 'label':'Minimum', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'maximum', 'label':'Maximum', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'average', 'label':'Average', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
    return line_chart_time_x(df, root, ['minimum','maximum','average'], ['time'], axes, 'Regional FOM Values')

def periods_of_partial_regional_satisfaction_interval_graph(stk_obj :FigureOfMerit, start_time=None, stop_time=None):
    r"""Createn Interval graph of the intervals of time when the region selected by the grid inspector is partially covered. A region is considered to be covered if at least one point within the region has access to one or more of the assigned assets. 

    This graph wrapper was generated from AGI\STK12\STKData\Styles\FigureOfMerit\GI Region Satisfaction.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Selected Region Partial Satisfaction').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    elements=[(('interval start', 'None'),('interval end', 'None'))]
    return interval_plot([df], elements, [], ['interval start','interval end'], 'Time', 'Periods of Partial Regional Satisfaction')

def overall_grid_statistics_time_xy_graph(stk_obj :FigureOfMerit, start_time=None, stop_time=None, step=60):
    r"""Create plot of the minimum, maximum, and average figure of merit values, sampled over all grid points, over time. Grid points for which a value cannot be computed are not included in the reported statistics.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\FigureOfMerit\Grid Stats Over Time.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Overall Value by Time').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'minimum', 'label':'Minimum', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'maximum', 'label':'Maximum', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'average', 'label':'Average', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
    return line_chart_time_x(df, root, ['minimum','maximum','average'], ['time'], axes, 'Overall Grid Statistics')

def satisfied_by_time_time_xy_graph(stk_obj :FigureOfMerit, start_time=None, stop_time=None, step=60):
    r"""Create plot of the percentage of the grid which satisfies the satisfaction criteria defined in the figure of merit, as a function of time.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\FigureOfMerit\Satisfied By Time.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Satisfied by Time').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percent satisfied', 'label':'% Satisfied', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
    return line_chart_time_x(df, root, ['percent satisfied'], ['time'], axes, 'Satisfied By Time')

def value_by_latitude_xy_graph(stk_obj : FigureOfMerit):
    r"""Create plot of the minimum, maximum, and average figure of merit value, sampled over all grid points at the same latitude, as a function of latitude. Statistics are generated by sampling values from all grid points with latitude values within one half degree of the reported latitude value. Values are computed for every one degree of latitude. For example, statistics reported for the latitude value of 30 degrees will represent figure of merit values for all points with latitudes between 29.5 and 30.5 degrees. Grid points for which a value cannot be computed are not included in the reported statistics. Latitudes which do not have any reported grid points within one half degree are not included in the reported values.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\FigureOfMerit\Value By Latitude.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Value by Latitude').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'minimum', 'label':'Minimum', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'maximum', 'label':'Maximum', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'average', 'label':'Average', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
    return line_chart(df, root, ['latitude','minimum','maximum','average'], [], axes, 'latitude','Latitude', 'Value By Latitude' )

def value_by_longitude_xy_graph(stk_obj : FigureOfMerit):
    r"""Create plot of the minimum, maximum, and average figure of merit value, sampled over all grid points at the same longitude, as a function of longitude. Statistics are generated by sampling values from all grid points with longitude values within one half degree of the reported longitude value. Values are computed for every one degree of longitude. For example, statistics reported for the longitude value of 30 degrees will represent figure of merit values for all points with longitudes between 29.5 and 30.5 degrees. Grid points for which a value cannot be computed are not included in the reported statistics. Longitudes which do not have any reported grid points within one half degree are not included in the reported values.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\FigureOfMerit\Value By Longitude.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Value by Longitude').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'minimum', 'label':'Minimum', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'maximum', 'label':'Maximum', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'},
            {'y_name':'average', 'label':'Average', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
    return line_chart(df, root, ['longitude','minimum','maximum','average'], [], axes, 'longitude','Longitude', 'Value By Longitude' )

