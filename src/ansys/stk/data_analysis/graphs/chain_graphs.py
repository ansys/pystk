"""Provides graphs for Chain objects."""
from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def chain_access_aer_time_xy_graph(stk_obj :Chain, start_time=None, stop_time=None, step=60):
    r"""Create plot of the azimuth, elevation, and range (AER) over time between access pairs in the strands of a Chain. The plot for each pair is shown over intervals that are the intersection of the pair's access intervals with the Chain's complete access intervals.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Chain\Access AER.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Access AER Data').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'azimuth', 'label':'Azimuth', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'},
            {'y_name':'elevation', 'label':'Elevation', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]},
            {'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'range', 'label':'Range', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]}]
    return line_chart_time_x(df, root, ['azimuth','elevation','range'], ['time'], axes, 'Chain Access AER')

def angle_between_data_time_xy_graph(stk_obj :Chain, start_time=None, stop_time=None, step=60):
    r"""Create plot of the angle and ranges for each three object sub-strand of a Chain, as a function of time, for each strand access interval that overlaps with the requested report time intervals.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Chain\Angle Between.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Angle Between').group.item('Granularity Determined').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'angle', 'label':'Angle', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]},
            {'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'range 1', 'label':'Range 1', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'},
            {'y_name':'range 2', 'label':'Range 2', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]}]
    return line_chart_time_x(df, root, ['angle','range 1','range 2'], ['time'], axes, 'Angle Between Data')

def bent_pipe_c_no_link_analysis_time_xy_graph(stk_obj :Chain, start_time=None, stop_time=None, step=60):
    r"""Graph shows the carrier-to-noise density ratio for uplink, downlink, and composite link as a function of time for a bent pipe communications system.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Chain\BentPipe Link - CNo.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Link Information').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Spectral Density', 'lines': [
            {'y_name':'c/no1', 'label':'C/No1', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'SpectralDensity'},
            {'y_name':'c/no tot.2', 'label':'C/No Tot.2', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'SpectralDensity'}]}]
    return line_chart_time_x(df, root, ['c/no1','c/no tot.2'], ['time'], axes, 'Bent Pipe C/No Link Analysis')

def complete_chain_access_times_interval_graph(stk_obj :Chain, start_time=None, stop_time=None):
    r"""Createn Interval plot of the time intervals for which the chain is completed. These intervals are computed by overlapping all the strand accesses.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Chain\Complete Chain Access.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Complete Access').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    elements=[(('start time', 'None'),('stop time', 'None'))]
    return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Complete Chain Access Times')

def object_access_interval_graph(stk_obj :Chain, start_time=None, stop_time=None):
    r"""Createn Interval graph of the time intervals for each object in a Chain for which the object participates in a strand that completes the chain. Each object's intervals are graphed on a separate line.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Chain\Individual Object Access.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Object Access').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    elements=[(('start time', 'None'),('stop time', 'None'))]
    return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Object Access')

def strand_access_times_interval_graph(stk_obj :Chain, start_time=None, stop_time=None):
    r"""Createn Interval graph of the time intervals for each strand in a Chain that completes the chain. Each strand's intervals are graphed on a separate line.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Chain\Individual Strand Access.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Strand Access').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    elements=[(('start time', 'None'),('stop time', 'None'))]
    return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Strand Access Times')

def number_of_accesses_time_xy_graph(stk_obj :Chain, start_time=None, stop_time=None, step=60):
    r"""Create plot of the number of objects participating in a strand that completes the chain at the given time, as a function of time. The report is only valid for Chains consisting of two objects.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\Chain\Number Of Accesses.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Base Object Data').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'number of accesses', 'label':'Number Of Accesses', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
    return line_chart_time_x(df, root, ['number of accesses'], ['time'], axes, 'Number Of Accesses')

