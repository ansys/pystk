"""Provides graphs for CommSystem objects."""
from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def carrier_to_noise_ratio_cdf_chart_xy_graph(stk_obj : CommSystem):
    r"""Graph shows the cumulative percentage of occurrence (CDF) as a function of carrier-to-noise ratio.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\CommSystem\Carrier to Noise CDF.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Cumulative Density Function').group.item('C/N').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percentage', 'label':'Percentage', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
    return line_chart(df, root, ['value','percentage'], [], axes, 'value','Value', 'Carrier to Noise Ratio CDF Chart' )

def carrier_to_noise_interference_ratio_cdf_chart_xy_graph(stk_obj : CommSystem):
    r"""Graph shows the cumulative percentage of occurrence (CDF) as a function of carrier-to-noise-plus-interference ratio.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\CommSystem\Carrier to Noise Interference CDF.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Cumulative Density Function').group.item('C/(N+I)').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percentage', 'label':'Percentage', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
    return line_chart(df, root, ['value','percentage'], [], axes, 'value','Value', 'Carrier to (Noise+Interference) Ratio CDF Chart' )

def carrier_to_noise_interference_ratio_pdf_xy_graph(stk_obj : CommSystem):
    r"""Graph shows the percentage of occurrence (PDF) as a function of carrier-to-noise-plus-interference ratio.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\CommSystem\Carrier to Noise Interference PDF.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Probability Density Function').group.item('C/(N+I)').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percentage', 'label':'Percentage', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
    return line_chart(df, root, ['value','percentage'], [], axes, 'value','Value', 'Carrier to (Noise+Interference) Ratio PDF' )

def carrier_to_noise_ratio_pdf_xy_graph(stk_obj : CommSystem):
    r"""Graph shows the percentage of occurrence (PDF) as a function of carrier-to-noise ratio.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\CommSystem\Carrier to Noise PDF.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Probability Density Function').group.item('C/N').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percentage', 'label':'Percentage', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
    return line_chart(df, root, ['value','percentage'], [], axes, 'value','Value', 'Carrier to Noise Ratio PDF' )

def carrier_to_noise_vs_time_time_xy_graph(stk_obj :CommSystem, start_time=None, stop_time=None, step=60):
    r"""Graph shows the carrier-to-noise ratio and the carrier-to-noise-plus-interference ratio as a function of time.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\CommSystem\Carrier to Noise vs Time.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Link Information').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'c/n', 'label':'C/N', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'},
            {'y_name':'c/(n+i)', 'label':'C/(N+I)', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Ratio'}]}]
    return line_chart_time_x(df, root, ['c/n','c/(n+i)'], ['time'], axes, 'Carrier to Noise vs Time')

def epfd_cdf_chart_xy_graph(stk_obj : CommSystem):
    r"""Graph shows the cumulative percentage of occurrence (CDF) as a function of power flux density.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\CommSystem\Power Flux Density CDF.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Cumulative Density Function').group.item('Pwr Flux Density').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': True, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percentage', 'label':'Percentage', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
    return line_chart(df, root, ['value','percentage'], [], axes, 'value','Value', 'EPFD CDF Chart' )

def epfd_xy_graph(stk_obj : CommSystem):
    r"""Graph shows the percentage of occurrence (PDF) as a function of power flux density.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\CommSystem\Power Flux Density PDF.rsg.
    """
    root = stk_obj.root
    df = stk_obj.data_providers.item('Probability Density Function').group.item('Pwr Flux Density').exec().data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': True, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percentage', 'label':'Percentage', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'Percent'}]}]
    return line_chart(df, root, ['value','percentage'], [], axes, 'value','Value', 'EPFD' )

