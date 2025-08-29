The ``missile_graphs`` module
==================================

.. py:module:: ansys.stk.extensions.data_analysis.graphs.missile_graphs

Summary
-------

.. tab-set::

    .. tab-item:: Functions

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.altitude_line_chart`
              - Plot the altitude of the object (i.e., magnitude of the relative position vector between the object and its detic subpoint) as a function of time

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.beta_angle_line_chart`
              - Plot the beta angle (i.e., the signed angle of the apparent vector to the Sun) over time, relative to the orbital plane.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.cumulative_sunlight_cumulative_pie_chart`
              - Create a pie chart showing the total duration of full sunlight within the graph's requested time interval.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.eclipse_times_interval_graph`
              - Create an interval graph of the penumbra (partial lighting) and umbra (zero lighting) intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.euler_angles_line_chart`
              - Create a plot of the attitude of the vehicle (i.e., the rotation between the vehicle's body axes and the vehicle' central body's inertial frame), expressed using 313 Euler angles, over time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.fixed_position_velocity_line_chart`
              - Plot the position and velocity of the object with respect to the object's central body, as observed from its central body's Fixed coordinate system, expressed in Cartesian components as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.j2000_position_velocity_line_chart`
              - Plot the position and velocity of the object with respect to the object's central body, as observed from its central body's J2000 coordinate system, expressed in Cartesian components as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.lighting_times_interval_graph`
              - Create an interval graph of the sunlight (full lighting) intervals, penumbra (partial lighting) intervals and umbra (zero lighting) intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.lla_position_line_chart`
              - Plot the position of the object, expressed in LLA elements, as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.model_area_line_chart`
              - Create a plot of the area of the object's 3D graphics model over time, as viewed from a given view direction, as computed by the Area Tool.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.re_entry_angle_line_chart`
              - Create a plot of the altitude and Re-entry Angle (i.e., the angle between the Fixed velocity direction of the object to the local horizontal plane), over time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.solar_aer_line_chart`
              - Create a plot of the azimuth, elevation, and range over time, describing the apparent relative position vector of the Sun with respect to Inertial VVLH axes (ECIVVLH).

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.solar_az_el_polar_center_0_graph`
              - Create a polar plot with elevation as radius and azimuth as angle theta over time, describing the apparent relative position vector of the Sun with respect to Inertial VVLH axes (ECIVVLH).

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.solar_intensity_line_chart`
              - Create a plot of the percent of the solar disc visible over time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.sun_vector_fixed_line_chart`
              - Create a plot of the apparent relative position of the Sun to the object, expressed in Cartesian components, using the object's central body's Fixed coordinate system, as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.sunlight_intervals_interval_pie_chart`
              - Create a pie chart showing each interval of full sunlight within the graph's requested time interval, separated by gaps indicating the intervals of penumbra/umbra lighting condition before and after each sunlight interval.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.missile_graphs.yaw_pitch_roll_line_chart`
              - Create a plot of the attitude of the vehicle (i.e., the rotation between the vehicle's body axes and the vehicle' central body's inertial frame), expressed using 321 YPR angles, as a function of time.

Description
-----------

Provides graphs for Missile objects.

.. py:currentmodule:: ansys.stk.extensions.data_analysis.graphs.missile_graphs

.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     altitude_line_chart<missile_graphs/altitude_line_chart>
     beta_angle_line_chart<missile_graphs/beta_angle_line_chart>
     cumulative_sunlight_cumulative_pie_chart<missile_graphs/cumulative_sunlight_cumulative_pie_chart>
     eclipse_times_interval_graph<missile_graphs/eclipse_times_interval_graph>
     euler_angles_line_chart<missile_graphs/euler_angles_line_chart>
     fixed_position_velocity_line_chart<missile_graphs/fixed_position_velocity_line_chart>
     j2000_position_velocity_line_chart<missile_graphs/j2000_position_velocity_line_chart>
     lighting_times_interval_graph<missile_graphs/lighting_times_interval_graph>
     lla_position_line_chart<missile_graphs/lla_position_line_chart>
     model_area_line_chart<missile_graphs/model_area_line_chart>
     re_entry_angle_line_chart<missile_graphs/re_entry_angle_line_chart>
     solar_aer_line_chart<missile_graphs/solar_aer_line_chart>
     solar_az_el_polar_center_0_graph<missile_graphs/solar_az_el_polar_center_0_graph>
     solar_intensity_line_chart<missile_graphs/solar_intensity_line_chart>
     sun_vector_fixed_line_chart<missile_graphs/sun_vector_fixed_line_chart>
     sunlight_intervals_interval_pie_chart<missile_graphs/sunlight_intervals_interval_pie_chart>
     yaw_pitch_roll_line_chart<missile_graphs/yaw_pitch_roll_line_chart>
