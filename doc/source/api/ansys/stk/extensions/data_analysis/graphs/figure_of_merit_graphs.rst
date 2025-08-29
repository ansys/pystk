The ``figure_of_merit_graphs`` module
==========================================

.. py:module:: ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs

Summary
-------

.. tab-set::

    .. tab-item:: Functions

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs.gi_all_dop_line_chart`
              - Create a plot of all DOP values, over time, for the point currently selected via the figure of merit grid inspector.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs.gi_point_fom_line_chart`
              - Create a plot of the figure of merit values over time, for the point currently selected via the figure of merit grid inspector.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs.gi_point_satisfaction_interval_graph`
              - Create an interval graph of the satisfaction intervals for the point currently selected via the figure of merit grid inspector.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs.gi_region_fom_line_chart`
              - Create a plot of the minimum, maximum, and average figure of merit value, sampled over all grid points within the region currently selected in the figure of merit grid inspector, over time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs.gi_region_satisfaction_interval_graph`
              - Create an interval graph of the intervals of time when the region selected by the grid inspector is partially covered.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs.grid_stats_over_time_line_chart`
              - Create a plot of the minimum, maximum, and average figure of merit values, sampled over all grid points, over time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs.satisfied_by_time_line_chart`
              - Create a plot of the percentage of the grid which satisfies the satisfaction criteria defined in the figure of merit, as a function of time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs.value_by_latitude_line_chart`
              - Create a plot of the minimum, maximum, and average figure of merit value, sampled over all grid points at the same latitude, as a function of latitude.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs.value_by_longitude_line_chart`
              - Create a plot of the minimum, maximum, and average figure of merit value, sampled over all grid points at the same longitude, as a function of longitude.

Description
-----------

Provides graphs for FigureOfMerit objects.

.. py:currentmodule:: ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs

.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     gi_all_dop_line_chart<figure_of_merit_graphs/gi_all_dop_line_chart>
     gi_point_fom_line_chart<figure_of_merit_graphs/gi_point_fom_line_chart>
     gi_point_satisfaction_interval_graph<figure_of_merit_graphs/gi_point_satisfaction_interval_graph>
     gi_region_fom_line_chart<figure_of_merit_graphs/gi_region_fom_line_chart>
     gi_region_satisfaction_interval_graph<figure_of_merit_graphs/gi_region_satisfaction_interval_graph>
     grid_stats_over_time_line_chart<figure_of_merit_graphs/grid_stats_over_time_line_chart>
     satisfied_by_time_line_chart<figure_of_merit_graphs/satisfied_by_time_line_chart>
     value_by_latitude_line_chart<figure_of_merit_graphs/value_by_latitude_line_chart>
     value_by_longitude_line_chart<figure_of_merit_graphs/value_by_longitude_line_chart>
