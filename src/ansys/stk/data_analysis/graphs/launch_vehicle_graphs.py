"""Provides graphs for LaunchVehicle objects."""
from ansys.stk.data_analysis.graphs.graph_functions import *
from ansys.stk.core.stkobjects import *

def altitude_time_xy_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Plot the altitude of the object (i.e., magnitude of the relative position vector between the object and its detic subpoint) as a function of time

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Altitude.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('LLA State').group.item('Fixed').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'alt', 'label':'Alt', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]}]
    return line_chart_time_x(df, root, ['alt'], ['time'], axes, 'Altitude')

def beta_angle_time_xy_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Plot the beta angle (i.e., the signed angle of the apparent vector to the Sun) over time, relative to the orbital plane. The signed angle is positive when the apparent vector is in the direction of the orbit normal. The orbit normal (which is normal to the orbital plane) is parallel to the orbital angular momentum vector, which is defined as the cross-product of the inertial position and velocity vectors.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Beta Angle.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Beta Angle').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'beta angle', 'label':'Beta Angle', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]}]
    return line_chart_time_x(df, root, ['beta angle'], ['time'], axes, 'Beta Angle')

def close_approach_periods_interval_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None):
    r"""Createn Interval graph of the conjunction time intervals where at least one conjunction occurs with a secondary vehicle, as computed by the Close Approach tool. A conjunction occurs if the object becomes with the specified minimum range threshold to a secondary vehicle at some time.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Close Approach Periods.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('CloseApproach').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    elements=[(('start time', 'None'),('end time', 'None'))]
    return interval_plot([df], elements, [], ['start time','end time'], 'Time', 'Close Approach Periods')

def cumulative_sunlight_cumulative_pie_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None):
    r"""Create Pie chart showing the total duration of full sunlight within the graph's requested time interval. Gaps in the chart indicate the total duration of penumbra and umbra durations.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Cumulative Sunlight.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Lighting Times').group.item('Sunlight').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Cumulative Sunlight', 'Time', True)

def eclipse_times_interval_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None):
    r"""Createn Interval graph of the penumbra (partial lighting) and umbra (zero lighting) intervals.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Eclipse Times.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Eclipse Times').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    elements=[(('start time', 'None'),('stop time', 'None'))]
    return interval_plot([df], elements, [], ['start time','stop time'], 'Time', 'Eclipse Times')

def euler_angles_time_xy_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Create plot of the attitude of the vehicle (i.e., the rotation between the vehicle's body axes and the vehicle' central body's inertial frame), expressed using 313 Euler angles, over time. Euler angles use a sequence of three rotations starting from a reference coordinate frame. The rotations are performed in succession: each rotation is relative to the frame resulting from any previous rotations. The 313 sequence uses Z, then the new X, and then finally the newest Z axis.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Euler Angles.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Euler Angles').group.item(0).exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'a', 'label':'A', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'},
            {'y_name':'b', 'label':'B', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'},
            {'y_name':'c', 'label':'C', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]}]
    return line_chart_time_x(df, root, ['a','b','c'], ['time'], axes, 'Euler Angles')

def fixed_position_velocity_time_xy_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Plot the position and velocity of the object with respect to the object's central body, as observed from its central body's Fixed coordinate system, expressed in Cartesian components as a function of time.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Fixed Position Velocity.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Cartesian Position').group.item('Fixed').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'x', 'label':'x', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'},
            {'y_name':'y', 'label':'y', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'},
            {'y_name':'z', 'label':'z', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]},
            {'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Rate', 'lines': [
            {'y_name':'vx', 'label':'vx', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Rate'},
            {'y_name':'vy', 'label':'vy', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Rate'},
            {'y_name':'vz', 'label':'vz', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Rate'}]}]
    return line_chart_time_x(df, root, ['x','y','z','vx','vy','vz'], ['time'], axes, 'Fixed Position & Velocity')

def j2000_position_velocity_time_xy_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Plot the position and velocity of the object with respect to the object's central body, as observed from its central body's J2000 coordinate system, expressed in Cartesian components as a function of time.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\J2000 Position Velocity.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Cartesian Position').group.item('J2000').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'x', 'label':'x', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'},
            {'y_name':'y', 'label':'y', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'},
            {'y_name':'z', 'label':'z', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]},
            {'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Rate', 'lines': [
            {'y_name':'vx', 'label':'vx', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Rate'},
            {'y_name':'vy', 'label':'vy', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Rate'},
            {'y_name':'vz', 'label':'vz', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Rate'}]}]
    return line_chart_time_x(df, root, ['x','y','z','vx','vy','vz'], ['time'], axes, 'J2000 Position & Velocity')

def launch_window_blackouts_interval_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None):
    r"""Createn Interval graph of the launch time intervals where at least one conjunction will occur with a secondary vehicle, if the object were to launch during that interval, as computed by the Launch Window tool. A conjunction occurs if the object would become with the specified minimum range threshold to a secondary vehicle at some later time.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Launch Window Blackouts.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('LaunchBlackout').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    elements=[(('blackout start time', 'None'),('blackout end time', 'None'))]
    return interval_plot([df], elements, [], ['blackout start time','blackout end time'], 'Time', 'Launch Window Blackouts')

def lighting_times_interval_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None):
    r"""Createn Interval graph of the sunlight (full lighting) intervals, penumbra (partial lighting) intervals and umbra (zero lighting) intervals. Each lighting condition's intervals are plotted on separate lines.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Lighting Times.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df_list=[]
    df_list.append(stk_obj.data_providers.item('Lighting Times').group.item('Sunlight').exec(start_time, stop_time).data_sets.to_pandas_dataframe())
    df_list.append(stk_obj.data_providers.item('Lighting Times').group.item('Penumbra').exec(start_time, stop_time).data_sets.to_pandas_dataframe())
    df_list.append(stk_obj.data_providers.item('Lighting Times').group.item('Umbra').exec(start_time, stop_time).data_sets.to_pandas_dataframe())
    elements=[(('start time', 'Sunlight'),('stop time', 'Sunlight')),(('start time', 'Penumbra'),('stop time', 'Penumbra')),(('start time', 'Umbra'),('stop time', 'Umbra'))]
    return interval_plot(df_list, elements, [], ['start time','stop time'], 'Time', 'Lighting Times')

def lla_position_time_xy_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Plot the position of the object, expressed in LLA elements, as a function of time. The coordinate system is the Fixed frame of the object's central body.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\LLA Position.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('LLA State').group.item('Fixed').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Latitude/Longitude', 'lines': [
            {'y_name':'lat', 'label':'Lat', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Latitude'},
            {'y_name':'lon', 'label':'Lon', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Longitude'}]},
            {'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'alt', 'label':'Alt', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]}]
    return line_chart_time_x(df, root, ['lat','lon','alt'], ['time'], axes, 'LLA Position')

def model_area_time_xy_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Create plot of the area of the object's 3D graphics model over time, as viewed from a given view direction, as computed by the Area Tool.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Model Area.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Model Area').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Area', 'lines': [
            {'y_name':'area', 'label':'Area', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Area'}]}]
    return line_chart_time_x(df, root, ['area'], ['time'], axes, 'Model Area')

def ecivvlh_solar_aer_time_xy_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Create plot of the azimuth, elevation, and range over time, describing the apparent relative position vector of the Sun with respect to Inertial VVLH axes (ECIVVLH).

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Solar AER.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Lighting AER').group.item('ECIVVLH').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'azimuth', 'label':'Azimuth', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'},
            {'y_name':'elevation', 'label':'Elevation', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]},
            {'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'range', 'label':'Range', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]}]
    return line_chart_time_x(df, root, ['azimuth','elevation','range'], ['time'], axes, 'ECIVVLH Solar AER')

def solar_ecf_vvlh_az_el_polar_center_0_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Create polar plot with elevation as radius and azimuth as angle theta over time, describing the apparent relative position vector of the Sun with respect to Inertial VVLH axes (ECIVVLH).

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Solar Az-El.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Lighting AER').group.item('ECFVVLH').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axis={'use_unit' : True, 'unit_squared': False, 'label': 'Angle', 'lines': [
        {'y_name':'elevation','x_name':'azimuth', 'label':'Azimuth', 'use_unit':True, 'unit_squared': False, 'unit_pref': 'Angle'}
        ]}
    return polar_chart(df, root, ['elevation','azimuth'], axis, 'Solar ECF VVLH Az-El', convert_negative_r = True, origin_0 = True )

def solar_intensity_time_xy_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Create plot of the percent of the solar disc visible over time.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Solar Intensity.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Solar Intensity').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'intensity', 'label':'Intensity', 'use_unit':False, 'unit_squared': None, 'unit_pref': 'None'}]}]
    return line_chart_time_x(df, root, ['intensity'], ['time'], axes, 'Solar Intensity')

def sun_vector_fixed_time_xy_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Create plot of the apparent relative position of the Sun to the object, expressed in Cartesian components, using the object's central body's Fixed coordinate system, as a function of time. 

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Sun Vector Fixed.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Sun Vector').group.item('Fixed').exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'x', 'label':'x', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'},
            {'y_name':'y', 'label':'y', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'},
            {'y_name':'z', 'label':'z', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Distance'}]}]
    return line_chart_time_x(df, root, ['x','y','z'], ['time'], axes, 'Sun Vector Fixed')

def sunlight_intervals_interval_pie_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None):
    r"""Create Pie chart showing each interval of full sunlight within the graph's requested time interval, separated by gaps indicating the intervals of penumbra/umbra lighting condition before and after each sunlight interval.

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Sunlight Intervals.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Lighting Times').group.item('Sunlight').exec(start_time, stop_time).data_sets.to_pandas_dataframe()
    return interval_pie_chart(root, df, ['duration'], ['start time','stop time'], 'start time', 'stop time', start_time, 'Sunlight Intervals', 'Time')

def ypr_time_xy_graph(stk_obj :LaunchVehicle, start_time=None, stop_time=None, step=60):
    r"""Create plot of the attitude of the vehicle (i.e., the rotation between the vehicle's body axes and the vehicle' central body's inertial frame), expressed using 321 YPR angles, as a function of time. YPR angles use a sequence of three rotations starting from a reference coordinate frame. Unlike Euler angles, the rotations are not made about axes defined by an earlier rotation: each rotation is made about the reference system's axes. The 321 sequence uses Z, then Y, and then finally the X axis. 

    This graph wrapper was generated from AGI\STK12\STKData\Styles\LaunchVehicle\Yaw Pitch Roll.rsg.
    """
    root = stk_obj.root
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
    df = stk_obj.data_providers.item('Attitude YPR').group.item(0).exec(start_time, stop_time, step).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'yaw', 'label':'Yaw', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'},
            {'y_name':'pitch', 'label':'Pitch', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'},
            {'y_name':'roll', 'label':'Roll', 'use_unit':None, 'unit_squared': None, 'unit_pref': 'Angle'}]}]
    return line_chart_time_x(df, root, ['yaw','pitch','roll'], ['time'], axes, 'YPR')

