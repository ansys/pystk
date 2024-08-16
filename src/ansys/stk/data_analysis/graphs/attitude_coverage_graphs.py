"""Provides graphs for AttitudeCoverage objects."""
from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def access_duration_xy_graph(stk_obj : IStkObject):
    r"""Create plot of the cumulative distribution of the access durations of all pointing directions. For each grid direction, access intervals to each assigned asset are combined to determine the time intervals over which at least one asset has access when pointed along the grid direction. The durations of these intervals, for all grid directions, are then sorted from smallest to largest and the percentages are then plotted.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\AttitudeCoverage\Access Duration.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Access Duration').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percent under', 'label':'% Under', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'},
            {'y_name':'percent over', 'label':'% Over', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
    return line_chart(df, root, ['percent under','percent over'], ['duration'], axes, 'duration','Duration', 'Access Duration' )

def coverage_by_latitude_xy_graph(stk_obj : IStkObject):
    r"""Create plot of the percent time covered vs latitude. A point is considered to be covered if it has access to one or more of the assigned assets. The reported values for each latitude are the average value for all grid points at that latitude.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\AttitudeCoverage\Coverage By Latitude.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Coverage by Latitude').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'percent time covered', 'label':'Percent Time Covered', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
    return line_chart(df, root, ['latitude','percent time covered'], [], axes, 'latitude','Latitude', 'Coverage By Latitude' )

def gap_duration_xy_graph(stk_obj : IStkObject):
    r"""Create plot of the cumulative distribution of the access duration gaps of all pointing directions. For each grid direction, access intervals to each assigned asset are combined to determine the time intervals over which at least one asset has access when pointed along the grid direction. The durations of the gaps between these intervals, for all grid directions, are then sorted from smallest to largest and the percentages are then plotted.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\AttitudeCoverage\Gap Duration.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Coverage Gap Duration').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percent under', 'label':'% Under', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'},
            {'y_name':'percent over', 'label':'% Over', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
    return line_chart(df, root, ['percent under','percent over'], ['duration'], axes, 'duration','Duration', 'Gap Duration' )

