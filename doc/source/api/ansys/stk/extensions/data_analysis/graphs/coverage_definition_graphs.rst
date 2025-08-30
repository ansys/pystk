The ``coverage_definition_graphs`` module
==============================================

.. py:module:: ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs

Summary
-------

.. tab-set::

    .. tab-item:: Functions

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.coverage_by_latitude_line_chart`
              - Create a plot of the percent time covered vs latitude.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.gap_duration_line_chart`
              - Create a plot of the cumulative distribution of the access duration gaps of all grid points.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.gi_point_coverage_interval_graph`
              - Create an interval graph of the access intervals for the point currently selected by the grid inspector.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.gi_point_prob_of_coverage_line_chart`
              - Create a plot of the probability of coverage being achieved for the point selected in the grid inspector, as a function of the time past a request for coverage.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.gi_region_coverage_line_chart`
              - Create a plot of the percentage of coverage over time of the region selected by the grid inspector.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.gi_region_full_coverage_interval_graph`
              - Create an interval graph of the intervals of time when the region selected by the grid inspector is completely covered.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.gi_region_time_to_cover_line_chart`
              - Create a plot of the amount of wait time required, starting from the reported time, before complete coverage of the region selected in the grid inspector occurs.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.percent_coverage_line_chart`
              - Create a plot of the percentage of the area of the total coverage grid which is covered at the reported time.

Description
-----------

Provides graphs for CoverageDefinition objects.

.. py:currentmodule:: ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs

.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     coverage_by_latitude_line_chart<coverage_definition_graphs/coverage_by_latitude_line_chart>
     gap_duration_line_chart<coverage_definition_graphs/gap_duration_line_chart>
     gi_point_coverage_interval_graph<coverage_definition_graphs/gi_point_coverage_interval_graph>
     gi_point_prob_of_coverage_line_chart<coverage_definition_graphs/gi_point_prob_of_coverage_line_chart>
     gi_region_coverage_line_chart<coverage_definition_graphs/gi_region_coverage_line_chart>
     gi_region_full_coverage_interval_graph<coverage_definition_graphs/gi_region_full_coverage_interval_graph>
     gi_region_time_to_cover_line_chart<coverage_definition_graphs/gi_region_time_to_cover_line_chart>
     percent_coverage_line_chart<coverage_definition_graphs/percent_coverage_line_chart>
