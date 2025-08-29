The ``satellite_graphs`` module
====================================

.. py:module:: ansys.stk.extensions.data_analysis.graphs.satellite_graphs

Summary
-------

.. tab-set::

    .. tab-item:: Functions

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.beta_angle_line_chart`
              - Plot the beta angle (i.e., the signed angle of the apparent vector to the Sun) over time, relative to the orbital plane.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.classical_orbit_elements_line_chart`
              - Create a plot of the angles and the semimajor axis of the classical osculating orbital elements, sometimes referred to as Keplerian elements, computed using ephemeris with respect to the object's J2000 coordinate system, as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.cumulative_sunlight_cumulative_pie_chart`
              - Create a pie chart showing the total duration of full sunlight within the graph's requested time interval.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.eclipse_times_interval_graph`
              - Create an interval graph of the penumbra (partial lighting) and umbra (zero lighting) intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.euler_angles_line_chart`
              - Create a plot of the attitude of the vehicle (i.e., the rotation between the vehicle's body axes and the vehicle' central body's inertial frame), expressed using 313 Euler angles, over time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.fixed_position_velocity_line_chart`
              - Plot the position and velocity of the object with respect to the object's central body, as observed from its central body's Fixed coordinate system, expressed in Cartesian components as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.inertial_position_velocity_line_chart`
              - Plot the position and velocity of the object with respect to the object's central body, as observed from its central body's inertial coordinate system, expressed in Cartesian components as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.j2000_position_velocity_line_chart`
              - Plot the position and velocity of the object with respect to the object's central body, as observed from its central body's J2000 coordinate system, expressed in Cartesian components as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.lighting_times_interval_graph`
              - Create an interval graph of the sunlight (full lighting) intervals, penumbra (partial lighting) intervals and umbra (zero lighting) intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.lla_position_line_chart`
              - Plot the position of the object, expressed in LLA elements, as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.model_area_line_chart`
              - Create a plot of the area of the object's 3D graphics model over time, as viewed from a given view direction, as computed by the Area Tool.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.solar_aer_line_chart`
              - Create a plot of the azimuth, elevation, and range over time, describing the apparent relative position vector of the Sun with respect to Inertial VVLH axes (ECIVVLH).

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.solar_az_el_polar_center_0_graph`
              - Create a polar plot with elevation as radius and azimuth as angle theta over time, describing the apparent relative position vector of the Sun with respect to Inertial VVLH axes (ECIVVLH).

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.solar_elevation_body_fixed_line_chart`
              - Create a plot of the solar elevation over time, describing the apparent relative position vector of the Sun with respect to the object.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.solar_intensity_line_chart`
              - Create a plot of the percent of the solar disc visible over time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.solar_panel_area_line_chart`
              - Create a plot of the effective area of the solar panels illuminated by the sun over time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.solar_panel_power_line_chart`
              - Create a plot of the power of the solar panels illuminated by the sun over time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.sun_vector_fixed_line_chart`
              - Create a plot of the apparent relative position of the Sun to the object, expressed in Cartesian components, using the object's central body's Fixed coordinate system, as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.sunlight_intervals_interval_pie_chart`
              - Create a pie chart showing each interval of full sunlight within the graph's requested time interval, separated by gaps indicating the intervals of penumbra/umbra lighting condition before and after each sunlight interval.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.tle_teme_residuals_line_chart`
              - Create a plot of the final residuals, computed between the object's position and the position created using the solved-for TLE created by the Generate TLE tool, as computed in the TEME coordinate systrem, as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.satellite_graphs.yaw_pitch_roll_line_chart`
              - Create a plot of the attitude of the vehicle (i.e., the rotation between the vehicle's body axes and the vehicle' central body's inertial frame), expressed using 321 YPR angles, as a function of time.

Description
-----------

Provides graphs for Satellite objects.

.. py:currentmodule:: ansys.stk.extensions.data_analysis.graphs.satellite_graphs

.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     beta_angle_line_chart<satellite_graphs/beta_angle_line_chart>
     classical_orbit_elements_line_chart<satellite_graphs/classical_orbit_elements_line_chart>
     cumulative_sunlight_cumulative_pie_chart<satellite_graphs/cumulative_sunlight_cumulative_pie_chart>
     eclipse_times_interval_graph<satellite_graphs/eclipse_times_interval_graph>
     euler_angles_line_chart<satellite_graphs/euler_angles_line_chart>
     fixed_position_velocity_line_chart<satellite_graphs/fixed_position_velocity_line_chart>
     inertial_position_velocity_line_chart<satellite_graphs/inertial_position_velocity_line_chart>
     j2000_position_velocity_line_chart<satellite_graphs/j2000_position_velocity_line_chart>
     lighting_times_interval_graph<satellite_graphs/lighting_times_interval_graph>
     lla_position_line_chart<satellite_graphs/lla_position_line_chart>
     model_area_line_chart<satellite_graphs/model_area_line_chart>
     solar_aer_line_chart<satellite_graphs/solar_aer_line_chart>
     solar_az_el_polar_center_0_graph<satellite_graphs/solar_az_el_polar_center_0_graph>
     solar_elevation_body_fixed_line_chart<satellite_graphs/solar_elevation_body_fixed_line_chart>
     solar_intensity_line_chart<satellite_graphs/solar_intensity_line_chart>
     solar_panel_area_line_chart<satellite_graphs/solar_panel_area_line_chart>
     solar_panel_power_line_chart<satellite_graphs/solar_panel_power_line_chart>
     sun_vector_fixed_line_chart<satellite_graphs/sun_vector_fixed_line_chart>
     sunlight_intervals_interval_pie_chart<satellite_graphs/sunlight_intervals_interval_pie_chart>
     tle_teme_residuals_line_chart<satellite_graphs/tle_teme_residuals_line_chart>
     yaw_pitch_roll_line_chart<satellite_graphs/yaw_pitch_roll_line_chart>
