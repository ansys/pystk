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

import collections
import typing

import matplotlib

from ansys.stk.core.stkobjects import STKObject
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import (
    interval_pie_chart,
    interval_plot,
    line_chart,
    pie_chart,
    polar_chart,
)


def _access_duration_pie_chart(stk_object :STKObject, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Access Data').execute_elements(start_time, stop_time, ['Duration', 'Access Number']).data_sets.to_pandas_dataframe()
    return pie_chart(root, df, ['duration'], [], 'duration', 'Access Duration', 'Time', 'access number', colormap = colormap)

def _cumulative_sunlight_cumulative_pie_chart(stk_object :STKObject, start_time: typing.Any = None, stop_time : typing.Any = None, color_list: list[typing.Any] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Lighting Times').group.item('Sunlight').execute_elements(start_time, stop_time, ['Duration', 'Stop Time', 'Start Time']).data_sets.to_pandas_dataframe()
    return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, stop_time, 'Cumulative Sunlight', 'Time', True, color_list = color_list)

def _eclipse_times_interval_graph(stk_object :STKObject, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Eclipse Times').execute_elements(start_time, stop_time, ['Start Time', 'Stop Time']).data_sets.to_pandas_dataframe()
    elements=[(('start time', 'None'),('stop time', 'None'))]
    return interval_plot([df], root, elements, [], ['start time','stop time'], 'Time', 'Eclipse Times', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _lighting_times_interval_graph(stk_object :STKObject, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df_list=[]
    df_list.append(stk_object.data_providers.item('Lighting Times').group.item('Sunlight').execute_elements(start_time, stop_time, ['Start Time', 'Stop Time']).data_sets.to_pandas_dataframe())
    df_list.append(stk_object.data_providers.item('Lighting Times').group.item('Penumbra').execute_elements(start_time, stop_time, ['Start Time', 'Stop Time']).data_sets.to_pandas_dataframe())
    df_list.append(stk_object.data_providers.item('Lighting Times').group.item('Umbra').execute_elements(start_time, stop_time, ['Start Time', 'Stop Time']).data_sets.to_pandas_dataframe())
    elements=[(('start time', 'Sunlight'),('stop time', 'Sunlight')),(('start time', 'Penumbra'),('stop time', 'Penumbra')),(('start time', 'Umbra'),('stop time', 'Umbra'))]
    return interval_plot(df_list, root, elements, [], ['start time','stop time'], 'Time', 'Lighting Times', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _lla_position_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('LLA State').group.item('Fixed').execute_elements(start_time, stop_time, step, ['Lon', 'Time', 'Alt', 'Lat']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Latitude/Longitude', 'lines': [
            {'y_name':'lat', 'label':'Lat', 'use_unit':True, 'unit_squared': None, 'dimension': 'Latitude'},
            {'y_name':'lon', 'label':'Lon', 'use_unit':True, 'unit_squared': None, 'dimension': 'Longitude'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'alt', 'label':'Alt', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'}]}]
    return line_chart([df], root, ['lat','lon','alt'], ['time'], axes, 'time', 'Time', 'LLA Position', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _model_area_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Model Area').execute_elements(start_time, stop_time, step, ['Time', 'Area']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Area', 'lines': [
            {'y_name':'area', 'label':'Area', 'use_unit':True, 'unit_squared': None, 'dimension': 'Area'}]}]
    return line_chart([df], root, ['area'], ['time'], axes, 'time', 'Time', 'Model Area', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _solar_aer_line_chart_stationary(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Lighting AER').execute_elements(start_time, stop_time, step, ['Time', 'Elevation', 'Range', 'Azimuth']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'elevation', 'label':'Elevation', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'range', 'label':'Range', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'}]}]
    return line_chart([df], root, ['azimuth','elevation','range'], ['time'], axes, 'time', 'Time', 'ECF VVLH Solar AER', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _solar_az_el_polar_center_0_graph_stationary(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Lighting AER').execute_elements(start_time, stop_time, step, ['Elevation', 'Azimuth']).data_sets.to_pandas_dataframe()
    axis={'use_unit' : True, 'unit_squared': False, 'label': 'Angle', 'lines': [
        {'y_name':'elevation','x_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': False, 'dimension': 'Angle'}
        ]}
    return polar_chart([df], root, ['elevation','azimuth'], axis, 'Solar ECF VVLH Az-El', convert_negative_r = True, origin_0 = False, colormap=colormap)

def _solar_aer_line_chart_vehicle(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Lighting AER').group.item('ECFVVLH').execute_elements(start_time, stop_time, step, ['Time', 'Elevation', 'Range', 'Azimuth']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'elevation', 'label':'Elevation', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'range', 'label':'Range', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'}]}]
    return line_chart([df], root, ['azimuth','elevation','range'], ['time'], axes, 'time', 'Time', 'ECF VVLH Solar AER', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _solar_az_el_polar_center_0_graph_vehicle(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Lighting AER').group.item('ECFVVLH').execute_elements(start_time, stop_time, step, ['Elevation', 'Azimuth']).data_sets.to_pandas_dataframe()
    axis={'use_unit' : True, 'unit_squared': False, 'label': 'Angle', 'lines': [
        {'y_name':'elevation','x_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': False, 'dimension': 'Angle'}
        ]}
    return polar_chart([df], root, ['elevation','azimuth'], axis, 'Solar ECF VVLH Az-El', convert_negative_r = True, origin_0 = False, colormap=colormap)

def _solar_intensity_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Solar Intensity').execute_elements(start_time, stop_time, step, ['Time', 'Intensity']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'intensity', 'label':'Intensity', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'}]}]
    return line_chart([df], root, ['intensity'], ['time'], axes, 'time', 'Time', 'Solar Intensity', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _solar_panel_area_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Solar Panel Area').execute_elements(start_time, stop_time, step, ['Time', 'Effective Area']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': True, 'ylog10': False, 'y2log10': False, 'label': ' Area', 'lines': [
            {'y_name':'effective area', 'label':'Effective Area', 'use_unit':True, 'unit_squared': True, 'dimension': 'SmallDistance'}]}]
    return line_chart([df], root, ['effective area'], ['time'], axes, 'time', 'Time', 'Area', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _solar_panel_power_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Solar Panel Power').execute_elements(start_time, stop_time, step, ['Time', 'Power']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Power', 'lines': [
            {'y_name':'power', 'label':'Power', 'use_unit':True, 'unit_squared': None, 'dimension': 'Power'}]}]
    return line_chart([df], root, ['power'], ['time'], axes, 'time', 'Time', 'Power', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _sun_vector_ecf_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Sun Vector').group.item('Fixed').execute_elements(start_time, stop_time, step, ['Time', 'x', 'y', 'z']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'x', 'label':'x', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'},
            {'y_name':'y', 'label':'y', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'},
            {'y_name':'z', 'label':'z', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'}]}]
    return line_chart([df], root, ['x','y','z'], ['time'], axes, 'time', 'Time', 'Sun Vector ECF', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _sunlight_intervals_interval_pie_chart(stk_object :STKObject, start_time: typing.Any = None, stop_time : typing.Any = None, color_list: list[typing.Any] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Lighting Times').group.item('Sunlight').execute_elements(start_time, stop_time, ['Duration', 'Stop Time', 'Start Time']).data_sets.to_pandas_dataframe()
    return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, stop_time, 'Sunlight Intervals', 'Time', color_list = color_list)

def _coverage_by_latitude_xy_graph(stk_object : STKObject, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    df = stk_object.data_providers.item('Coverage by Latitude').execute_elements(['Latitude', 'Percent Time Covered']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'percent time covered', 'label':'Percent Time Covered', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'}]}]
    return line_chart([df], root, ['latitude','percent time covered'], [], axes, 'latitude','Latitude', 'Coverage By Latitude', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _gap_duration_xy_graph(stk_object : STKObject, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    df = stk_object.data_providers.item('Coverage Gap Duration').execute_elements(['Duration', 'Percent Under', 'Percent Over']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percent under', 'label':'% Under', 'use_unit':False, 'unit_squared': None, 'dimension': 'Percent'},
            {'y_name':'percent over', 'label':'% Over', 'use_unit':False, 'unit_squared': None, 'dimension': 'Percent'}]}]
    return line_chart([df], root, ['percent under','percent over', 'duration'], [], axes, 'duration','Duration', 'Gap Duration', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _grid_stats_over_time_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Overall Value by Time').execute_elements(start_time, stop_time, step, ['Time', 'Minimum', 'Maximum', 'Average']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'minimum', 'label':'Minimum', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'maximum', 'label':'Maximum', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'average', 'label':'Average', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]}]
    return line_chart([df], root, ['minimum','maximum','average'], ['time'], axes, 'time', 'Time', 'Grid Stats Over Time', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _value_by_latitude_xy_graph(stk_object : STKObject, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    df = stk_object.data_providers.item('Value by Latitude').execute_elements(['Maximum', 'Minimum', 'Latitude', 'Average']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'minimum', 'label':'Minimum', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'maximum', 'label':'Maximum', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'average', 'label':'Average', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]}]
    return line_chart([df], root, ['latitude','minimum','maximum','average'], [], axes, 'latitude','Latitude', 'Value By Latitude', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _value_by_longitude_xy_graph(stk_object : STKObject, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    df = stk_object.data_providers.item('Value by Longitude').execute_elements(['Minimum', 'Maximum', 'Longitude', 'Average']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'minimum', 'label':'Minimum', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'maximum', 'label':'Maximum', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'average', 'label':'Average', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]}]
    return line_chart([df], root, ['longitude','minimum','maximum','average'], [], axes, 'longitude','Longitude', 'Value By Longitude', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _lat_lon_position_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('LLA State').group.item('Fixed').execute_elements(start_time, stop_time, step, ['Lon', 'Time', 'Lat']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Latitude/Longitude', 'lines': [
            {'y_name':'lat', 'label':'Lat', 'use_unit':True, 'unit_squared': None, 'dimension': 'Latitude'},
            {'y_name':'lon', 'label':'Lon', 'use_unit':True, 'unit_squared': None, 'dimension': 'Longitude'}]}]
    return line_chart([df], root, ['lat','lon'], ['time'], axes, 'time', 'Time', 'Lat-Lon Position', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _altitude_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('LLA State').group.item('Fixed').execute_elements(start_time, stop_time, step, ['Time', 'Alt']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'alt', 'label':'Alt', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'}]}]
    return line_chart([df], root, ['alt'], ['time'], axes, 'time', 'Time', 'Altitude', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _beta_angle_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Beta Angle').execute_elements(start_time, stop_time, step, ['Time', 'Beta Angle']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'beta angle', 'label':'Beta Angle', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]}]
    return line_chart([df], root, ['beta angle'], ['time'], axes, 'time', 'Time', 'Beta Angle', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _euler_angles_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Euler Angles').group.item(0).execute_elements(start_time, stop_time, step, ['Time', 'C', 'A', 'B']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'a', 'label':'A', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'b', 'label':'B', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'c', 'label':'C', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]}]
    return line_chart([df], root, ['a','b','c'], ['time'], axes, 'time', 'Time', 'Euler Angles', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _fixed_position_velocity_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = []
    data.append(stk_object.data_providers.item('Cartesian Position').group.item('Fixed').execute_elements(start_time, stop_time, step, ['Time', 'x', 'y', 'z']).data_sets.to_pandas_dataframe())
    data.append(stk_object.data_providers.item('Cartesian Velocity').group.item('Fixed').execute_elements(start_time, stop_time, step, ['Time', 'x', 'y', 'z']).data_sets.to_pandas_dataframe())
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'x', 'label':'x', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'},
            {'y_name':'y', 'label':'y', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'},
            {'y_name':'z', 'label':'z', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Rate', 'lines': [
            {'y_name':'x', 'label':'vx', 'use_unit':True, 'unit_squared': None, 'dimension': 'Rate'},
            {'y_name':'y', 'label':'vy', 'use_unit':True, 'unit_squared': None, 'dimension': 'Rate'},
            {'y_name':'z', 'label':'vz', 'use_unit':True, 'unit_squared': None, 'dimension': 'Rate'}]}]
    return line_chart(data, root, [['x','y','z'],['x','y','z']], ['time'], axes, 'time', 'Time', 'Fixed Position & Velocity', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter, multiple_data_providers=True)

def _j2000_position_velocity_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = []
    data.append(stk_object.data_providers.item('Cartesian Position').group.item('J2000').execute_elements(start_time, stop_time, step, ['Time', 'x', 'y', 'z']).data_sets.to_pandas_dataframe())
    data.append(stk_object.data_providers.item('Cartesian Velocity').group.item('J2000').execute_elements(start_time, stop_time, step, ['Time', 'x', 'y', 'z']).data_sets.to_pandas_dataframe())

    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'x', 'label':'x', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'},
            {'y_name':'y', 'label':'y', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'},
            {'y_name':'z', 'label':'z', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Rate', 'lines': [
            {'y_name':'x', 'label':'vx', 'use_unit':True, 'unit_squared': None, 'dimension': 'Rate'},
            {'y_name':'y', 'label':'vy', 'use_unit':True, 'unit_squared': None, 'dimension': 'Rate'},
            {'y_name':'z', 'label':'vz', 'use_unit':True, 'unit_squared': None, 'dimension': 'Rate'}]}]
    return line_chart(data, root, [['x','y','z'],['x','y','z']], ['time'], axes, 'time', 'Time', 'J2000 Position & Velocity', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter, multiple_data_providers=True)

def _sun_vector_fixed_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Sun Vector').group.item('Fixed').execute_elements(start_time, stop_time, step, ['Time', 'x', 'y', 'z']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'x', 'label':'x', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'},
            {'y_name':'y', 'label':'y', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'},
            {'y_name':'z', 'label':'z', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'}]}]
    return line_chart([df], root, ['x','y','z'], ['time'], axes, 'time', 'Time', 'Sun Vector Fixed', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _yaw_pitch_roll_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Attitude YPR').group.item(0).execute_elements(start_time, stop_time, step, ['Yaw', 'Time', 'Pitch', 'Roll']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'yaw', 'label':'Yaw', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'pitch', 'label':'Pitch', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'},
            {'y_name':'roll', 'label':'Roll', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]}]
    return line_chart([df], root, ['yaw','pitch','roll'], ['time'], axes, 'time', 'Time', 'YPR', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def _azimuth_elevation_line_chart(stk_object :STKObject, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Boresight AzEl').execute_elements(start_time, stop_time, step, ['Parent Rel Azimuth', 'Parent Rel Elevation', 'Time']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'parent rel azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'parent rel elevation', 'label':'Elevation', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]}]
    return line_chart([df], root, ['parent rel azimuth','parent rel elevation'], ['time'], axes, 'time', 'Time', 'Azimuth-Elevation', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)