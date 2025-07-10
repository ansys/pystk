The ``access_graphs`` module
=================================

.. py:module:: ansys.stk.extensions.data_analysis.graphs.access_graphs

Summary
-------

.. tab-set::

    .. tab-item:: Functions

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.access_duration_pie_chart`
              - Create pie chart of the durations of the access intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.access_interval_graph`
              - Create an interval graph of the access intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.aer_line_chart`
              - Create plot of the azimuth, elevation, and range values for the relative position vector between the base object and the target object, during access intervals. The relative position includes the effects of light time delay and aberration as set by the computational settings of the access. Az-El values are computed with respect to the default AER frame of the selected object of the Access Tool.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.az_el_polar_center_90_graph`
              - Create a polar plot with elevation as radius and azimuth as angle theta over time, during access intervals. The azimuth and elevation describe the relative position vector between the base object and the target object. The relative position includes the effects of light time delay and aberration as set by the computational settings of the access. Az-El values are computed with respect to the default AER frame of the selected object of the Access Tool.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.cumulative_dwell_cumulative_pie_chart`
              - Create graph showing access interval durations as a cumulative pie chart.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.revisit_diagram_interval_pie_chart`
              - Create pie chart showing the durations of access intervals and access gap intervals.

Description
-----------

Provides graphs for Access objects.

.. py:currentmodule:: ansys.stk.extensions.data_analysis.graphs.access_graphs

.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     access_duration_pie_chart<access_graphs/access_duration_pie_chart>
     access_interval_graph<access_graphs/access_interval_graph>
     aer_line_chart<access_graphs/aer_line_chart>
     az_el_polar_center_90_graph<access_graphs/az_el_polar_center_90_graph>
     cumulative_dwell_cumulative_pie_chart<access_graphs/cumulative_dwell_cumulative_pie_chart>
     revisit_diagram_interval_pie_chart<access_graphs/revisit_diagram_interval_pie_chart>
