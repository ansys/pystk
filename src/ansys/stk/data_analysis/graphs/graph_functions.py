import pandas as pd
import matplotlib.dates as md
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from math import radians

def line_chart(df, root, numerical_columns, time_columns, axes, x_column, x_label, title, groupby=None):
    num_lines = 0
    for axis in axes:
        num_lines += len(axis['lines'])
    unit_preferences = root.unit_preferences
    fig, ax = plt.subplots()
    df = convert_columns(df, numerical_columns, time_columns)
    df.dropna(axis=0, inplace=True)
    df.sort_values(x_column, inplace=True)
    mpl_lines = []
    colors = plt.cm.rainbow(np.linspace(0, 1, num_lines))
    line_count = 0
    x_data = df[x_column]
    axes_list = [ax]
    for i in range(len(axes)):
        axis = axes[i]
        if i != 0:
            ax = ax.twinx()
            axes_list.append(ax)
        for j in range(len(axis['lines'])):
            line = axis['lines'][j]
            y_data = df[line['y_name']]
            label = line['label']
            if line['use_unit']:
                unit_pref = unit_preferences.get_current_unit_abbrv(line['unit_pref'])
                if line['unit_squared']:
                    label = label + f"({unit_pref}^2)"
                else:
                    label = label + f"({unit_pref})"
            if groupby:
                df.groupby(groupby).plot(x=x_column, y=line['y_name'], ax=ax, label=label, color=colors[line_count])
            else:
                mpl_lines.extend(ax.plot(x_data, y_data, label=label, color=colors[line_count]))
            line_count += 1
        if axis['use_unit']:
                if axis['unit_squared']:
                    ax.set_ylabel(axis['label'] + f" ({unit_pref}^2)")
                else:
                    ax.set_ylabel(axis['label'] + f" ({unit_pref})")
        else:
            ax.set_ylabel(axis['label'])

        ax.set_xlabel(x_label)

        ax.set_facecolor('whitesmoke')

        if len(axes) == 1:
            ax.grid(visible=True, axis='both', which='both', linestyle='--')
        else:
            ax.grid(visible=True, axis='x', which='both', linestyle='--')

        if axis['ylog10']:
            ax.set_yscale('log')
        elif axis['y2log10']:
            ax.set_yscale('log', base=2)

    if groupby and num_lines > 1:
        groupby_legend(axes_list)
    if num_lines > 1:
        ax.legend(mpl_lines, [l.get_label() for l in mpl_lines], shadow=True)

    ax.set_title(title)
    fig.set_size_inches(12, 6)
    return fig, ax


def line_chart_time_x(df, root, numerical_columns, time_columns, axes, title, groupby = None):
    num_lines = 0
    for axis in axes:
        num_lines += len(axis['lines'])
    unit_preferences = root.unit_preferences
    fig, ax = plt.subplots()
    df = convert_columns(df, numerical_columns, time_columns)
    df.sort_values('time', inplace=True)
    df.dropna(axis=0, inplace=True)
    mpl_lines = []
    colors = plt.cm.rainbow(np.linspace(0, 1, num_lines))
    line_count = 0
    x_data = df['time']
    axes_list = [ax]
    for i in range(len(axes)):
        axis = axes[i]
        if i != 0:
            ax = ax.twinx()
            axes_list.append(ax)
        for j in range(len(axis['lines'])):
            line = axis['lines'][j]
            y_data = df[line['y_name']]
            label = line['label']
            if line['use_unit']:
                unit_pref = unit_preferences.get_current_unit_abbrv(line['unit_pref'])
                if line['unit_squared']:
                    label = label + f"({unit_pref}^2)"
                else:
                    label = label + f"({unit_pref})"
            if groupby:
                df.groupby(groupby).plot(x='time', y=line['y_name'], ax=ax, label=label, color=colors[line_count])
            else:
                mpl_lines.extend(ax.plot(x_data, y_data, label=label, color=colors[line_count]))
            line_count += 1
        if axis['use_unit']:
            if axis['unit_squared']:
                ax.set_ylabel(axis['label'] + f" ({unit_pref}^2)")
            else:
                ax.set_ylabel(axis['label'] + f" ({unit_pref})")
        else:
            ax.set_ylabel(axis['label'])

        ax.set_xlabel('Time')

        ax.set_facecolor('whitesmoke')

        if len(axes) == 1:
            ax.grid(visible=True, axis='both', which='both', linestyle='--')
        else:
            ax.grid(visible=True, axis='x', which='both', linestyle='--')

        if axis['ylog10']:
            ax.set_yscale('log')
        elif axis['y2log10']:
            ax.set_yscale('log', base=2)

    if groupby and num_lines > 1:
        groupby_legend(axes_list)
    if num_lines > 1:
        ax.legend(mpl_lines, [l.get_label() for l in mpl_lines], shadow=True)

    format_time_axis(ax, df, 'time')

    ax.set_title(title)
    fig.set_size_inches(12, 6)
    return fig, ax    

# only supports plotting a single column
def polar_chart(df, root, numerical_columns, axis, title, origin_0 = False, convert_negative_r = False, groupby=None):
    df = convert_columns(df, numerical_columns, [])
    df.dropna(axis=0, inplace=True)
    # matplotlib works in radians
    x_column = line = axis['lines'][0]['x_name']
    df[x_column] = df[x_column].apply(lambda x : radians(x))

    line = axis['lines'][0]
    y_var = line['y_name']
    
    # matplotlib doesn't support negative r values in polar graphs, so convert for stk graphs
    # that show negative r values with negative angle
    if convert_negative_r:
        eliminate_negative_r_polar_vals(df, y_var, x_column)

    unit_preferences = root.unit_preferences
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    num_lines = len(axis['lines'])
    if groupby:
        colors = plt.cm.rainbow(np.linspace(0,1,len(df.groupby(groupby))))
    else:
        colors = plt.cm.rainbow(np.linspace(0,1,num_lines))

    if line['use_unit']:
        unit_pref = unit_preferences.get_current_unit_abbrv(line['unit_pref'])
        if line['unit_squared']:
            label = line['label'] + f"({unit_pref}^2)"
        else:
            label = line['label'] + f"({unit_pref})"

    if groupby:
        group_count = 0
        for element, group in df.groupby(groupby):
            group.plot(x_column, y_var, color=colors[group_count], label = f"{element}", ax=ax)
            group_count += 1
    else:
        x_data = df[x_column]
        y_data = df[y_var]
        ax.plot(x_data, y_data, label=label, color=colors[0])

    ax.set_xlabel(f"{axis['label']} ({unit_pref})")
    ax.set_facecolor('whitesmoke')
    ax.grid(visible=True, axis='both', which='both', linestyle='--')
    ax.set_title(title)

    ax.set_theta_direction(-1)

    # styling for y axis with negative values to match stk styling
    if not convert_negative_r:
        ax.set_ylim(-70, 90)
        ax.invert_yaxis()

    if origin_0:
        ax.set_theta_zero_location('N')

    if groupby:
        ax.legend(ax.get_lines(), [l.get_label() for l in ax.get_lines()], shadow=True, loc=(1.05, 0.98), title=groupby, ncols=int(len(df.groupby(groupby))/3))

    return fig, ax

def interval_plot(df_list, element_pairs : list, numerical_columns : list, time_columns : list, x_label : str, title : str):
    fig, ax = plt.subplots()
    bar_num = 0
    colors = plt.cm.rainbow(np.linspace(0,1,len(element_pairs)))
    bars = []
    tick_locs = []
    for i in range(len(element_pairs)):
        element_pair = element_pairs[i]
        first_elem = element_pair[0]
        second_elem = element_pair[1]
        df = df_list[i]
        convert_columns(df, numerical_columns, time_columns)
        df['graph duration'] = df[second_elem[0]] - df[first_elem[0]]
        bars.append(ax.broken_barh(list(zip(df[first_elem[0]], df['graph duration'])), (bar_num*10 + 10, 9), facecolors=colors[bar_num], label=first_elem[1] if first_elem[1] else ''))
        tick_locs.append(bar_num*10 + 14.5)
        bar_num += 1
    format_time_axis(ax, df, element_pair[0][0])
    ax.set_xlabel(f"{x_label}")
    if len(element_pairs) > 1:
        ax.legend(bars, [b.get_label() for b in bars], shadow=True)
    ax.set_title(title)
    ax.set_facecolor('whitesmoke')
    ax.grid(visible=True, axis='both', which='both', linestyle='--')
    ax.set_axisbelow(True)
    ax.set_yticks(tick_locs, labels = [b.get_label() for b in bars])
    ax.get_yaxis().set_visible(False)
    fig.set_size_inches(18.5, 7)
    return fig, ax

def pie_chart(root, df, numerical_columns : list, time_columns : list, column : str, title : str, unit_pref : str, label_col=None):
    fig, ax = plt.subplots()
    unit_preferences = root.unit_preferences
    unit_pref = unit_preferences.get_current_unit_abbrv(unit_pref)
    df = convert_columns(df, numerical_columns, time_columns)
    df.dropna(axis=0, inplace=True)
    num_colors_needed = len(df[column].value_counts())
    colors = plt.cm.rainbow(np.linspace(0,1,num_colors_needed))
    if label_col:
        labels= []
        for i in range(len(df[label_col])):
            labels.append(f"{label_col} {df[label_col][i]}: {df[column][i]:.3f}({unit_pref})")
    else:
        labels=[f"{val:.3f}({unit_pref})" for val in df[column]]
    ax.pie(df[column], autopct='%1.1f%%', labels=labels, colors=colors)
    ax.set_title(title)
    return fig, ax

def interval_pie_chart(root, df, numerical_columns : list, time_columns : list, start_col : str, stop_col : str, start_time : str, title:str, unit_pref:str, cumulative=False):
    df = convert_columns(df, numerical_columns, time_columns)
    df['duration'] = df[stop_col] - df[start_col]
    df['gap'] = df[start_col].shift(-1) - df[stop_col]
    df['duration'] = df['duration'] / np.timedelta64(1, 's')
    df['gap'] = df['gap'] / np.timedelta64(1, 's')
    unit_preferences = root.unit_preferences
    unit_pref = unit_preferences.get_current_unit_abbrv(unit_pref)
    fig, ax = plt.subplots()
    if cumulative:
        duration_sum = df['duration'].sum()
        gap_sum = df['gap'].sum() + ((pd.to_datetime(df['start time'][0]) - pd.to_datetime(start_time)) / np.timedelta64(1, 's'))
        plt.pie([duration_sum, gap_sum], labels=[f"Cumulative Duration: {duration_sum:.2f} ({unit_pref})", f"Cumulative Gap: {gap_sum:.2f} ({unit_pref})"], colors=['deepskyblue','slategray'], autopct='%1.3f%%', labeldistance=None, pctdistance=1.2)
        ax.legend(shadow=True, loc='lower center')
    else:
        zip_list = list(zip(df['duration'], df['gap']))
        flat_list = []
        label_list = []
        count = 2
        for item in zip_list:
            flat_list.append(item[0])
            if not np.isnan(item[0]):
                label_list.append(f"duration {count -1}: {item[0]:.2f}({unit_pref})")
            flat_list.append(item[1])
            if not np.isnan(item[1]):
                label_list.append(f"gap {count}: {item[1]:.2f}({unit_pref})")
            count += 1
        cleaned_list = [x for x in flat_list if not np.isnan(x)]
        first_gap = (pd.to_datetime(df['start time'][0]) - pd.to_datetime(start_time)) / np.timedelta64(1, 's')
        cleaned_list.insert(0, first_gap)
        label_list.insert(0, f"gap 1: {first_gap:.2f}({unit_pref})")
        plt.pie(cleaned_list, labels=label_list, colors=['slategray', 'deepskyblue'], autopct='%1.3f%%', labeldistance=1.4, pctdistance=1.1)
        fig.set_size_inches(8, 8)
        ax.legend(ncol=len(cleaned_list)/4, loc=(0, -0.1), shadow=True, fontsize="x-small")
    ax.set_title(title)
    return fig, ax

def convert_columns(dataframe, numerical_column_list, date_column_list):
    for column in numerical_column_list:
        dataframe[column] = pd.to_numeric(dataframe[column])
    for column in date_column_list:
        dataframe[column] = pd.to_datetime(dataframe[column])
    return dataframe

def format_time_axis(ax, dataframe, time_col_name):
    dataframe.sort_values(by=time_col_name)
    first_time = dataframe.iloc[0][time_col_name]
    last_time = dataframe.iloc[-1][time_col_name]
    time_diff = last_time - first_time
    if time_diff < dt.timedelta(minutes=10):
        formatter = md.DateFormatter("%M:%S.%f")
        xlocator_major = md.MinuteLocator(interval=1)
        xlocator_minor = md.SecondLocator(interval=30)
    elif time_diff < dt.timedelta(hours=1):
        formatter = md.DateFormatter('%M:%S')
        xlocator_major = md.MinuteLocator(interval=10)
        xlocator_minor = md.MinuteLocator(interval=5)
    elif time_diff < dt.timedelta(hours=24):
        formatter = md.DateFormatter('%H:%M:%S')
        xlocator_major = md.HourLocator(interval=2)
        xlocator_minor = md.HourLocator(interval=1)
    elif time_diff < dt.timedelta(hours=48):
        formatter = md.DateFormatter('%H:%M:%S')
        xlocator_major = md.HourLocator(interval=4)
        xlocator_minor = md.HourLocator(interval=2)
    elif time_diff < dt.timedelta(days=365):
        formatter = md.DateFormatter('%M %D %H:%M:%S')
        xlocator_major = md.DayLocator(interval=60)
        xlocator_minor = md.DayLocator(interval=30)
    else:
        formatter = md.DateFormatter('%M %D %Y %H:%M:%S')
        xlocator_major = md.DayLocator(interval=90)
        xlocator_minor = md.DayLocator(interval=30)

    ax.xaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_locator(xlocator_major)
    ax.xaxis.set_minor_locator(xlocator_minor)

def eliminate_negative_r_polar_vals(df, r_var, theta_var):
    df[theta_var]= np.where(df[r_var] >= 0, df[theta_var], df[theta_var] + np.pi)
    df[r_var] = df[r_var].apply(lambda x: abs(x))

def groupby_legend(axes):
    handles, labels = axes[0].get_legend_handles_labels()
    for i in range(1, len(axes)):
        ax_handles, ax_labels = axes[i].get_legend_handles_labels()
        handles.extend(ax_handles)
        labels.extend(ax_labels)
    unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
    axes[0].legend(*zip(*unique))
    