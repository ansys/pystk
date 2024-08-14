import pandas as pd
import matplotlib.dates as md
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from math import radians

def line_chart(df, root, numerical_columns, time_columns, axes, x_column, x_label, title, groupby=None):
    """Creates a line chart from the provided dataframe and axes information."""
    # count number of lines
    num_lines = 0
    for axis in axes:
        num_lines += len(axis['lines'])

    # get unit preferences from root
    unit_preferences = root.unit_preferences

    # create plot
    fig, ax = plt.subplots()

    # data conversions
    df = convert_columns(df, numerical_columns, time_columns)
    df.dropna(axis=0, inplace=True)
    df.sort_values(x_column, inplace=True)

    # line collection for legend
    mpl_lines = []

    # create color map with correct length
    colors = plt.cm.rainbow(np.linspace(0, 1, num_lines))

    # used to count line number to subset color map
    line_count = 0

    # get x data from dataframe
    x_data = df[x_column]

    # add matplotlib axis to list
    axes_list = [ax]

    # iterate through axes information parameter
    for i in range(len(axes)):
        axis = axes[i]
        # if additional axes needed, duplicated matplotlib axis
        if i != 0:
            ax = ax.twinx()
            axes_list.append(ax)
        # iterate through lines under axis
        for j in range(len(axis['lines'])):
            line = axis['lines'][j]
            # get y data
            y_data = df[line['y_name']]
            # get line label
            label = line['label']
            # if line uses unit, get current unit
            if line['use_unit']:
                unit_pref = unit_preferences.get_current_unit_abbrv(line['unit_pref'])
                # check if unit should be squared in label
                if line['unit_squared']:
                    label = label + f"({unit_pref}^2)"
                else:
                    label = label + f"({unit_pref})"
            # if data is grouped, group in dataframe then plot x and y
            if groupby:
                df.groupby(groupby).plot(x=x_column, y=line['y_name'], ax=ax, label=label, color=colors[line_count])
            # if data is ungrouped, plot individual line
            else:
                mpl_lines.extend(ax.plot(x_data, y_data, label=label, color=colors[line_count]))
            line_count += 1
        # if axis uses unit, set unit in label
        if axis['use_unit']:
                if axis['unit_squared']:
                    ax.set_ylabel(axis['label'] + f" ({unit_pref}^2)")
                else:
                    ax.set_ylabel(axis['label'] + f" ({unit_pref})")
        else:
            ax.set_ylabel(axis['label'])

        # set x-label
        ax.set_xlabel(x_label)

        # set styling (must be done for each axis)
        ax.set_facecolor('whitesmoke')

        if len(axes) == 1:
            ax.grid(visible=True, axis='both', which='both', linestyle='--')
        # if multiple axes, only plot x gridlines
        else:
            ax.grid(visible=True, axis='x', which='both', linestyle='--')

        # set axis scales
        if axis['ylog10']:
            ax.set_yscale('log')
        elif axis['y2log10']:
            ax.set_yscale('log', base=2)

    # if plot is grouped with multiple lines, create configured legend
    if groupby and num_lines > 1:
        groupby_legend(axes_list)
    # if multiple lines, create legend
    if num_lines > 1:
        ax.legend(mpl_lines, [l.get_label() for l in mpl_lines], shadow=True)

    # set title and size
    ax.set_title(title)
    fig.set_size_inches(12, 6)
    # return figure and axis
    return fig, ax


def line_chart_time_x(df, root, numerical_columns, time_columns, axes, title, groupby = None):
    """Creates a line chart from the provided dataframe and axes information, with an x-axis corresponding to time."""
    # count number of lines
    num_lines = 0
    for axis in axes:
        num_lines += len(axis['lines'])

    # get unit preferences from root
    unit_preferences = root.unit_preferences

    # create plot
    fig, ax = plt.subplots()

    # data conversions
    df = convert_columns(df, numerical_columns, time_columns)
    df.sort_values('time', inplace=True)
    df.dropna(axis=0, inplace=True)

    # line collection for legend
    mpl_lines = []

    # create color map with correct length
    colors = plt.cm.rainbow(np.linspace(0, 1, num_lines))

    # used to count line number to subset color map
    line_count = 0

    # get x data from dataframe -> always time for this type of chart
    x_data = df['time']

    # add matplotlib axis to list
    axes_list = [ax]

    # iterate through axes information parameter
    for i in range(len(axes)):
        axis = axes[i]
        # if additional axes needed, duplicated matplotlib axis
        if i != 0:
            ax = ax.twinx()
            axes_list.append(ax)
        # iterate through lines under axis
        for j in range(len(axis['lines'])):
            line = axis['lines'][j]
            # get y data
            y_data = df[line['y_name']]
            # get line label
            label = line['label']
            # if line uses unit, get current unit
            if line['use_unit']:
                unit_pref = unit_preferences.get_current_unit_abbrv(line['unit_pref'])
                # check if unit should be squared in label
                if line['unit_squared']:
                    label = label + f"({unit_pref}^2)"
                else:
                    label = label + f"({unit_pref})"
            # if data is grouped, group in dataframe then plot x and y
            if groupby:
                df.groupby(groupby).plot(x='time', y=line['y_name'], ax=ax, label=label, color=colors[line_count])
            # if data is ungrouped, plot individual line
            else:
                mpl_lines.extend(ax.plot(x_data, y_data, label=label, color=colors[line_count]))
            line_count += 1
        # if axis uses unit, set unit in label
        if axis['use_unit']:
            if axis['unit_squared']:
                ax.set_ylabel(axis['label'] + f" ({unit_pref}^2)")
            else:
                ax.set_ylabel(axis['label'] + f" ({unit_pref})")
        else:
            ax.set_ylabel(axis['label'])

        # set x-label
        ax.set_xlabel('Time')

        # set styling (must be done for each axis)
        ax.set_facecolor('whitesmoke')

        if len(axes) == 1:
            ax.grid(visible=True, axis='both', which='both', linestyle='--')
        # if multiple axes, only plot x gridlines
        else:
            ax.grid(visible=True, axis='x', which='both', linestyle='--')

        # set axis scales
        if axis['ylog10']:
            ax.set_yscale('log')
        elif axis['y2log10']:
            ax.set_yscale('log', base=2)

    # if plot is grouped with multiple lines, create configured legend
    if groupby and num_lines > 1:
        groupby_legend(axes_list)
    # if multiple lines, create legend
    if num_lines > 1:
        ax.legend(mpl_lines, [l.get_label() for l in mpl_lines], shadow=True)

    # format x-axis to display well with times
    format_time_axis(ax, df, 'time')

    # set title and size
    ax.set_title(title)
    fig.set_size_inches(12, 6)

    # return figure and axis
    return fig, ax    

# only supports plotting a single column
def polar_chart(df, root, numerical_columns, axis, title, origin_0 = False, convert_negative_r = False, groupby=None):
    """Create a polar chart from the provided dataframe and axis information. Only supports plotting one x:y data pair."""

    # data conversions
    df = convert_columns(df, numerical_columns, [])
    df.dropna(axis=0, inplace=True)

    # matplotlib works in radians, so get x (theta) column and convert
    x_column = axis['lines'][0]['x_name']
    df[x_column] = df[x_column].apply(lambda x : radians(x))

    # get line information
    line = axis['lines'][0]
    # get y (r) variable
    y_var = line['y_name']
    
    # matplotlib doesn't support negative r values in polar graphs, so convert for stk graphs
    # that show negative r values with negative angle
    if convert_negative_r:
        eliminate_negative_r_polar_vals(df, y_var, x_column)

    # get unit preferences from root 
    unit_preferences = root.unit_preferences

    # create plot
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # get number of lines
    num_lines = len(axis['lines'])

    # if grouping by other column, each group should have separate color
    if groupby:
        colors = plt.cm.rainbow(np.linspace(0,1,len(df.groupby(groupby))))
    # else, use one color per line
    else:
        colors = plt.cm.rainbow(np.linspace(0,1,num_lines))

    # if line uses unit, get current unit 
    if line['use_unit']:
        unit_pref = unit_preferences.get_current_unit_abbrv(line['unit_pref'])
        if line['unit_squared']:
            label = line['label'] + f"({unit_pref}^2)"
        else:
            label = line['label'] + f"({unit_pref})"

    # if grouped, plot each group
    if groupby:
        group_count = 0
        for element, group in df.groupby(groupby):
            group.plot(x_column, y_var, color=colors[group_count], label = f"{element}", ax=ax)
            group_count += 1
    # if not grouped, plot x and y data
    else:
        x_data = df[x_column]
        y_data = df[y_var]
        ax.plot(x_data, y_data, label=label, color=colors[0])

    # set x label
    ax.set_xlabel(f"{axis['label']} ({unit_pref})")
    # set styling
    ax.set_facecolor('whitesmoke')
    ax.grid(visible=True, axis='both', which='both', linestyle='--')
    # set title
    ax.set_title(title)
    # set theta direction to match stk
    ax.set_theta_direction(-1)

    # styling for y axis with negative values to match stk styling
    if not convert_negative_r:
        ax.set_ylim(-70, 90)
        ax.invert_yaxis()

    # configure origin location to march stk
    if origin_0:
        ax.set_theta_zero_location('N')

    # grouped by legend, no legend needed otherwise
    if groupby:
        ax.legend(ax.get_lines(), [l.get_label() for l in ax.get_lines()], shadow=True, loc=(1.05, 0.98), title=groupby, ncols=int(len(df.groupby(groupby))/3))

    # return figure and axis
    return fig, ax

def interval_plot(df_list, element_pairs : list, numerical_columns : list, time_columns : list, x_label : str, title : str):
    """Creates an interval plot from the provided list of dataframes."""
    # create plot
    fig, ax = plt.subplots()

    # count number of bars
    bar_num = 0

    # create color map with one color for each bar
    colors = plt.cm.rainbow(np.linspace(0,1,len(element_pairs)))

    # collect bars
    bars = []

    # collect y tick locations
    tick_locs = []

    # iterate through pairs of elements
    for i in range(len(element_pairs)):
        element_pair = element_pairs[i]
        first_elem = element_pair[0]
        second_elem = element_pair[1]
        # get corresponding dataframe
        df = df_list[i]
        # convert columns for each dataframe
        convert_columns(df, numerical_columns, time_columns)
        # add column to dataframe with difference between end and start times
        df['graph duration'] = df[second_elem[0]] - df[first_elem[0]]
        # create bar starting at start times with length corresponding to duration
        # label if label provided, otherwise leave blank
        bars.append(ax.broken_barh(list(zip(df[first_elem[0]], df['graph duration'])), (bar_num*10 + 10, 9), facecolors=colors[bar_num], label=first_elem[1] if first_elem[1] else ''))
        # append tick location
        tick_locs.append(bar_num*10 + 14.5)
        bar_num += 1

    # format time axis
    format_time_axis(ax, df, element_pair[0][0], element_pair[1][0])

    # set x label
    ax.set_xlabel(f"{x_label}")

    # create legend if more than one bar
    if len(element_pairs) > 1:
        ax.legend(bars, [b.get_label() for b in bars], shadow=True)

    # set title
    ax.set_title(title)

    # set styling
    ax.set_facecolor('whitesmoke')
    ax.grid(visible=True, axis='both', which='both', linestyle='--')
    ax.set_axisbelow(True)

    # label y-axis using tick locations
    ax.set_yticks(tick_locs, labels = [b.get_label() for b in bars])

    # hide y-axis
    ax.get_yaxis().set_visible(False)

    # set size
    fig.set_size_inches(18.5, 7)

    # return figure and axis
    return fig, ax

def pie_chart(root, df, numerical_columns : list, time_columns : list, column : str, title : str, unit_pref : str, label_col=None):
    """Creates a pie chart from the provided dataframe and information."""
    # create plot
    fig, ax = plt.subplots()

    # get unit
    unit_preferences = root.unit_preferences
    unit_pref = unit_preferences.get_current_unit_abbrv(unit_pref)

    # data conversions
    df = convert_columns(df, numerical_columns, time_columns)
    df.dropna(axis=0, inplace=True)

    # create colormap with one color for each slice of pie
    num_colors_needed = len(df[column].value_counts())
    colors = plt.cm.rainbow(np.linspace(0,1,num_colors_needed))

    # if plot is labeled with a different column, get and configure labels
    if label_col:
        labels= []
        for i in range(len(df[label_col])):
            labels.append(f"{label_col} {df[label_col][i]}: {df[column][i]:.3f}({unit_pref})")
    # else label with column values and unit
    else:
        labels=[f"{val:.3f}({unit_pref})" for val in df[column]]

    # create pie chart
    ax.pie(df[column], autopct='%1.1f%%', labels=labels, colors=colors)

    # set title
    ax.set_title(title)

    # return figure and axis
    return fig, ax

def interval_pie_chart(root, df, numerical_columns : list, time_columns : list, start_col : str, stop_col : str, start_time : str, title:str, unit_pref:str, cumulative=False):
    """Creates an interval pie chart from the provided dataframe."""
    # data conversions
    df = convert_columns(df, numerical_columns, time_columns)

    # create duration column using stop and start columns
    df['graph duration'] = df[stop_col] - df[start_col]

    # create gap column with times in between durations
    df['graph gap'] = df[start_col].shift(-1) - df[stop_col]

    # convert duration and graph columns to time delta objects in seconds
    df['graph duration'] = df['graph duration'] / np.timedelta64(1, 's')
    df['graph gap'] = df['graph gap'] / np.timedelta64(1, 's')

    # get unit preferences
    unit_preferences = root.unit_preferences
    unit_pref = unit_preferences.get_current_unit_abbrv(unit_pref)

    # create plot
    fig, ax = plt.subplots()
    if cumulative:
        # if plot is cumulative, sum durations and gaps
        duration_sum = df['graph duration'].sum()
        # for gap sum, add gap before first duration begins
        gap_sum = df['graph gap'].sum() + ((pd.to_datetime(df['start time'][0]) - pd.to_datetime(start_time)) / np.timedelta64(1, 's'))
        # plot duration and gap sums
        plt.pie([duration_sum, gap_sum], labels=[f"Cumulative Duration: {duration_sum:.2f} ({unit_pref})", f"Cumulative Gap: {gap_sum:.2f} ({unit_pref})"], colors=['deepskyblue','slategray'], autopct='%1.3f%%', labeldistance=None, pctdistance=1.2)
        # create legend
        ax.legend(shadow=True, loc='lower center')
    else:
        # create zipped list with each duration and gap paired
        zip_list = list(zip(df['graph duration'], df['graph gap']))
        flat_list = []
        label_list = []
        count = 2
        # flatten list while maintaining order
        # at the same time, create list of labels
        for item in zip_list:
            flat_list.append(item[0])
            if not np.isnan(item[0]):
                label_list.append(f"duration {count -1}: {item[0]:.2f}({unit_pref})")
            flat_list.append(item[1])
            if not np.isnan(item[1]):
                label_list.append(f"gap {count}: {item[1]:.2f}({unit_pref})")
            count += 1
        # remove any nan values
        cleaned_list = [x for x in flat_list if not np.isnan(x)]
        # get gap before start of first interval, add to data and label lists
        first_gap = (pd.to_datetime(df['start time'][0]) - pd.to_datetime(start_time)) / np.timedelta64(1, 's')
        cleaned_list.insert(0, first_gap)
        label_list.insert(0, f"gap 1: {first_gap:.2f}({unit_pref})")
        # plot intervals
        plt.pie(cleaned_list, labels=label_list, colors=['slategray', 'deepskyblue'], autopct='%1.3f%%', labeldistance=1.4, pctdistance=1.1)
        # set size
        fig.set_size_inches(8, 8)
        # create legend
        ax.legend(ncol=len(cleaned_list)/4, loc=(0, -0.1), shadow=True, fontsize="x-small")

    # set title
    ax.set_title(title)
    
    # return figure and axis
    return fig, ax

def convert_columns(dataframe, numerical_column_list, date_column_list):
    """Converts numerical and time columns in a pandas dataframe."""
    for column in numerical_column_list:
        dataframe[column] = pd.to_numeric(dataframe[column])
    for column in date_column_list:
        dataframe[column] = pd.to_datetime(dataframe[column])
    return dataframe

def format_time_axis(ax, dataframe, time_col_name, time_col_name2=None):
    """Formats a matplotlib axis to display well with time."""
    dataframe.sort_values(by=time_col_name)
    first_time = dataframe.iloc[0][time_col_name]
    if time_col_name2:
        last_time = dataframe.iloc[-1][time_col_name2]
    else:
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
    """Converts negative r values in a dataframe that has r and theta values."""
    df[theta_var]= np.where(df[r_var] >= 0, df[theta_var], df[theta_var] + np.pi)
    df[r_var] = df[r_var].apply(lambda x: abs(x))

def groupby_legend(axes):
    """Creates a legend from grouped data."""
    handles, labels = axes[0].get_legend_handles_labels()
    for i in range(1, len(axes)):
        ax_handles, ax_labels = axes[i].get_legend_handles_labels()
        handles.extend(ax_handles)
        labels.extend(ax_labels)
    unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
    axes[0].legend(*zip(*unique))
    