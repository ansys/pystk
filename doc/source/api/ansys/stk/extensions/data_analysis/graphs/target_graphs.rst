The ``target_graphs`` module
=================================

.. py:module:: ansys.stk.extensions.data_analysis.graphs.target_graphs

Summary
-------

.. tab-set::

    .. tab-item:: Functions

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.target_graphs.cumulative_sunlight_cumulative_pie_chart`
              - Create a pie chart showing the total duration of full sunlight within the graph's requested time interval.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.target_graphs.eclipse_times_interval_graph`
              - Create an interval graph of the penumbra (partial lighting) and umbra (zero lighting) intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.target_graphs.lighting_times_interval_graph`
              - Create an interval graph of the sunlight (full lighting) intervals, penumbra (partial lighting) intervals and umbra (zero lighting) intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.target_graphs.model_area_line_chart`
              - Create a plot of the area of the object's 3D graphics model over time, as viewed from a given view direction, as computed by the Area Tool.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.target_graphs.solar_aer_line_chart`
              - Create a plot of the azimuth, elevation, and range over time, describing the apparent relative position vector of the Sun with respect to the local horizontal plane.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.target_graphs.solar_az_el_polar_center_0_graph`
              - Create a polar plot with elevation as radius and azimuth as angle theta over time, describing the apparent relative position vector of the Sun with respect to the local horizontal plane.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.target_graphs.sunlight_intervals_interval_pie_chart`
              - Create a pie chart showing each interval of full sunlight within the graph's requested time interval, separated by gaps indicating the intervals of penumbra/umbra lighting condition before and after each sunlight interval.

Description
-----------

Provides graphs for Target objects.

.. py:currentmodule:: ansys.stk.extensions.data_analysis.graphs.target_graphs

.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     cumulative_sunlight_cumulative_pie_chart<target_graphs/cumulative_sunlight_cumulative_pie_chart>
     eclipse_times_interval_graph<target_graphs/eclipse_times_interval_graph>
     lighting_times_interval_graph<target_graphs/lighting_times_interval_graph>
     model_area_line_chart<target_graphs/model_area_line_chart>
     solar_aer_line_chart<target_graphs/solar_aer_line_chart>
     solar_az_el_polar_center_0_graph<target_graphs/solar_az_el_polar_center_0_graph>
     sunlight_intervals_interval_pie_chart<target_graphs/sunlight_intervals_interval_pie_chart>
