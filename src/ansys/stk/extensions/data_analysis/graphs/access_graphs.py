# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Provides graphs for Access objects."""

import collections.abc
import typing

import matplotlib

from ansys.stk.core.stkobjects import Access
from ansys.stk.extensions.data_analysis.graphs._common_graphs import _access_duration_pie_chart
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import (
    _get_access_data,
    interval_pie_chart,
    interval_plot,
    line_chart,
    polar_chart,
)


def access_duration_pie_chart(stk_object :Access, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a pie chart of the durations of the access intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Access Duration.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    return _access_duration_pie_chart(stk_object, start_time, stop_time, colormap)

def access_interval_graph(stk_object :Access, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the access intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Access.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Access Data').execute_elements(start_time, stop_time, ['Start Time', 'Stop Time']).data_sets.to_pandas_dataframe()
    elements=[(('start time', 'None'),('stop time', 'None'))]
    return interval_plot([df], root, elements, [], ['start time','stop time'], 'Time', 'Access Times', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def aer_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the azimuth, elevation, and range values for the relative position vector between the base object and the target object, during access intervals.

    The relative position includes the effects of light time delay and aberration as set by the computational settings of the access. Az-El values are computed with respect to the default AER frame of the selected object of the Access Tool.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\AER.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'AER Data', True, 'Default', ['Time', 'Elevation', 'Azimuth', 'Range'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Longitude/Angle', 'lines': [
            {'y_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': None, 'dimension': 'Longitude'},
            {'y_name':'elevation', 'label':'Elevation', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'range', 'label':'Range', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'}]}]
    return line_chart(data, root, ['azimuth','elevation','range'], ['time'], axes, 'time', 'Time', 'AER', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def angular_rates_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the azimuth rate, elevation rate, and angular rate over time, during each access interval, from the perspective of the selected object in the Access Tool.

    The azimuth rate, elevation rate, and angular rate are available only if the selected object supports that metric as an access constraint: the value being reported is that as computed by that access constraint.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Angular Rates.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Constraint Data', False, None, ['FromElevationRate', 'Time', 'FromAngularRate', 'FromAzimuthRate'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle Rate', 'lines': [
            {'y_name':'fromangularrate', 'label':'FromAngularRate', 'use_unit':True, 'unit_squared': None, 'dimension': 'AngleRate'},
            {'y_name':'fromazimuthrate', 'label':'FromAzimuthRate', 'use_unit':True, 'unit_squared': None, 'dimension': 'AngleRate'},
            {'y_name':'fromelevationrate', 'label':'FromElevationRate', 'use_unit':True, 'unit_squared': None, 'dimension': 'AngleRate'}]}]
    return line_chart(data, root, ['fromangularrate','fromazimuthrate','fromelevationrate'], ['time'], axes, 'time', 'Time', 'Angular Rates', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def az_el_polar_center_90_graph(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a polar plot with elevation as radius and azimuth as angle theta over time, during access intervals.

    The azimuth and elevation describe the relative position vector between the base object and the target object. The relative position includes the effects of light time delay and aberration as set by the computational settings of the access. Az-El values are computed with respect to the default AER frame of the selected object of the Access Tool.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Az El Polar.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'AER Data', True, 0, ['Elevation', 'Azimuth'], start_time, stop_time, step)
    axis={'use_unit' : True, 'unit_squared': False, 'label': 'Angle', 'lines': [
        {'y_name':'elevation','x_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': False, 'dimension': 'Angle'}
        ]}
    return polar_chart(data, root, ['elevation','azimuth'], axis, 'Az El Polar', convert_negative_r = False, origin_0 = True, colormap=colormap)

def bit_error_rate_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Plot the bit error rate (BER) over time, during each access interval.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Bit_Error_Rate.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Link Information', False, None, ['Time', 'BER'], start_time, stop_time, step)
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'ber', 'label':'BER', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'}]}]
    return line_chart(data, root, ['ber'], ['time'], axes, 'time', 'Time', 'Bit Error Rate', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def carrier_to_noise_ratio_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Plot the carrier to noise ratio (C/N) over time, during each access interval.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Carrier_to_Noise_Ratio.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Link Information', False, None, ['Time', 'C/N'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'c/n', 'label':'C/N', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'}]}]
    return line_chart(data, root, ['c/n'], ['time'], axes, 'time', 'Time', 'Carrier to Noise Ratio', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def cumulative_dwell_cumulative_pie_chart(stk_object :Access, start_time: typing.Any = None, stop_time : typing.Any = None, color_list: list[typing.Any] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph access interval durations as a cumulative pie chart.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Cumulative Dwell.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    color_list : list of typing.Any
        The colors with which to color the pie chart slices (the default is None). Must have length >= 2.

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Access Data').execute_elements(start_time, stop_time, ['Access Number', 'Stop Time', 'Start Time', 'Duration']).data_sets.to_pandas_dataframe()
    return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, stop_time, 'Cumulative Dwell', 'Time', True, color_list = color_list)

def ebno_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Plot the energy per bit to noise ratio (Eb/No) over time, during each access interval.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\EbNo.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Link Information', False, None, ['Eb/No', 'Time'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'eb/no', 'label':'Eb/No', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'}]}]
    return line_chart(data, root, ['eb/no'], ['time'], axes, 'time', 'Time', 'EbNo', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def elevation_angle_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the elevation angle and its rate over time, during each access interval, from the perspective of the selected object in the Access Tool.

    The elevation angle value is that as computed by the elevation constraint for the selected object. The elevation rate is available only if the selected object supports that metric as an access constraint: the value being reported is that as computed by that access constraint.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Elevation Angle.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Constraint Data', False, None, ['FromElevationRate', 'Time', 'FromElevationAngle'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'fromelevationangle', 'label':'FromElevationAngle', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle Rate', 'lines': [
            {'y_name':'fromelevationrate', 'label':'FromElevationRate', 'use_unit':True, 'unit_squared': None, 'dimension': 'AngleRate'}]}]
    return line_chart(data, root, ['fromelevationangle','fromelevationrate'], ['time'], axes, 'time', 'Time', 'Elevation', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def gaps_interval_graph(stk_object :Access, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the intervals where access does not exist between the objects.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Gaps.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Access Gaps').execute_elements(start_time, stop_time, ['Start Time', 'Stop Time']).data_sets.to_pandas_dataframe()
    elements=[(('start time', 'None'),('stop time', 'None'))]
    return interval_plot([df], root, elements, [], ['start time','stop time'], 'Time', 'Access Gap Periods', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def probability_of_detection_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph the probability of a radar pulse search detection versus time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Probability_of_Detection.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Radar SearchTrack', False, None, ['Time', 'S/T PDet1'], start_time, stop_time, step)
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'s/t pdet1', 'label':'S/T PDet1', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'}]}]
    return line_chart(data, root, ['s/t pdet1'], ['time'], axes, 'time', 'Time', 'Probability of Detection', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def radar_antenna_gain_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph the antenna gain (value toward the Az, El direction)for both receiver and transmitter versus time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Radar Antenna Gain.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Radar Antenna', False, None, ['Time', 'Rcvr Ant Gain', 'Xmtr Ant Gain'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'rcvr ant gain', 'label':'Rcvr Ant Gain', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'xmtr ant gain', 'label':'Xmtr Ant Gain', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'}]}]
    return line_chart(data, root, ['rcvr ant gain','xmtr ant gain'], ['time'], axes, 'time', 'Time', 'Radar Antenna Gain', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def radar_propagation_loss_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph the receive and transmit total propagation attenuation values for the primary polarization signal channel versus time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Radar Propagation Loss.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Radar Environment', False, None, ['Time', 'Rcvr Prop Atten', 'Xmtr Prop Atten'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'rcvr prop atten', 'label':'Rcvr Prop Atten', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'},
            {'y_name':'xmtr prop atten', 'label':'Xmtr Prop Atten', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'}]}]
    return line_chart(data, root, ['rcvr prop atten','xmtr prop atten'], ['time'], axes, 'time', 'Time', 'Radar Propagation Loss', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def radar_sar_azimuth_resolution_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph the radar SAR azimuth resolution and SAR integration time versus time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Radar SAR Azimuth Resolution.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Radar SAR', False, None, ['Time', 'SAR Integration Time', 'SAR Az Resolution'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'sar az resolution', 'label':'SAR Az Resolution', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Time', 'lines': [
            {'y_name':'sar integration time', 'label':'SAR Integration Time', 'use_unit':True, 'unit_squared': None, 'dimension': 'Time'}]}]
    return line_chart(data, root, ['sar az resolution','sar integration time'], ['time'], axes, 'time', 'Time', 'Radar SAR Azimuth Resolution', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def radar_sar_time_resolution_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph the time-varying data for the SAR time-resolution product.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Radar SAR Time-Resolution.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Radar SAR', False, None, ['Time', 'SAR Time-Resolution Prod'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Sar Time Res Prod', 'lines': [
            {'y_name':'sar time-resolution prod', 'label':'SAR Time-Resolution Prod', 'use_unit':True, 'unit_squared': None, 'dimension': 'SarTimeResProd'}]}]
    return line_chart(data, root, ['sar time-resolution prod'], ['time'], axes, 'time', 'Time', 'Radar SAR Time-Resolution', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def radar_searchtrack_integration_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph time-varying data for the following radar SearchTrack parameters: S/T integration time, S/T dwell time, and S/T pulses integrated.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Radar SearchTrack Integration.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Radar SearchTrack', False, None, ['Time', 'S/T Dwell Time', 'S/T Integration Time', 'S/T Pulses Integrated'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': ' Time', 'lines': [
            {'y_name':'s/t integration time', 'label':'S/T Integration Time', 'use_unit':True, 'unit_squared': None, 'dimension': 'SmallTime'},
            {'y_name':'s/t dwell time', 'label':'S/T Dwell Time', 'use_unit':True, 'unit_squared': None, 'dimension': 'SmallTime'}]},
            {'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'s/t pulses integrated', 'label':'S/T Pulses Integrated', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'}]}]
    return line_chart(data, root, ['s/t integration time','s/t dwell time','s/t pulses integrated'], ['time'], axes, 'time', 'Time', 'Radar SearchTrack Integration', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def radar_searchtrack_snr_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph radar SearchTrack signal-to-noise ratio versus time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Radar SearchTrack SNR.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Radar SearchTrack', False, None, ['Time', 'S/T SNR1'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'s/t snr1', 'label':'S/T SNR1', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'}]}]
    return line_chart(data, root, ['s/t snr1'], ['time'], axes, 'time', 'Time', 'Radar SearchTrack SNR', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def radar_system_noise_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph the antenna noise temperature and total noise temperature versus time for a radar receiver.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Radar System Noise.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Radar Environment', False, None, ['System Temp', 'Time', 'Antenna Temp'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Temperature', 'lines': [
            {'y_name':'antenna temp', 'label':'Antenna Temp', 'use_unit':True, 'unit_squared': None, 'dimension': 'Temperature'},
            {'y_name':'system temp', 'label':'System Temp', 'use_unit':True, 'unit_squared': None, 'dimension': 'Temperature'}]}]
    return line_chart(data, root, ['antenna temp','system temp'], ['time'], axes, 'time', 'Time', 'Radar System Noise', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def revisit_diagram_interval_pie_chart(stk_object :Access, start_time: typing.Any = None, stop_time : typing.Any = None, color_list: list[typing.Any] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a pie chart showing the durations of access intervals and access gap intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Revisit Diagram.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    color_list : list of typing.Any
        The colors with which to color the pie chart slices (the default is None). Must have length >= 2.

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Access Data').execute_elements(start_time, stop_time, ['Access Number', 'Stop Time', 'Start Time', 'Duration']).data_sets.to_pandas_dataframe()
    return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, stop_time, 'Revisit Diagram', 'Time', color_list = color_list)

def signal_to_noise_ratio_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Plot the search track signal to noise ratio (S/N) over time, during each access interval.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Signal_to_Noise_Ratio.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Radar SearchTrack', False, None, ['Time', 'S/T SNR1'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'s/t snr1', 'label':'S/T SNR1', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'}]}]
    return line_chart(data, root, ['s/t snr1'], ['time'], axes, 'time', 'Time', 'Signal to Noise Ratio', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def sun_rfi_line_chart(stk_object :Access, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph the sun-induced antenna noise temperature as well as the receiver gain to system temperature ratio at the receiver as a function of time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Sun RFI.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, 'Link Information', False, None, ['Time', 'Tsun', 'g/T'], start_time, stop_time, step)
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Temperature', 'lines': [
            {'y_name':'tsun', 'label':'Tsun', 'use_unit':True, 'unit_squared': None, 'dimension': 'Temperature'}]},
            {'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'g/t', 'label':'g/T (dB/K)', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'}]}]
    return line_chart(data, root, ['tsun','g/t'], ['time'], axes, 'time', 'Time', 'Sun RFI', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

