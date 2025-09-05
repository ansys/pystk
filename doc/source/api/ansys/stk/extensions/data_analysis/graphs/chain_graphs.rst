The ``chain_graphs`` module
================================

.. py:module:: ansys.stk.extensions.data_analysis.graphs.chain_graphs

Summary
-------

.. tab-set::

    .. tab-item:: Functions

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.chain_graphs.angle_between_line_chart`
              - Create a plot of the angle and ranges for each three object sub-strand of a Chain, as a function of time, for each strand access interval that overlaps with the requested report time intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.chain_graphs.bentpipe_link_cno_line_chart`
              - Graph the carrier-to-noise density ratio for uplink, downlink, and composite link as a function of time for a bent pipe communications system.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.chain_graphs.complete_chain_access_interval_graph`
              - Create an interval plot of the time intervals for which the chain is completed.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.chain_graphs.individual_object_access_interval_graph`
              - Create an interval graph of the time intervals for each object in a Chain for which the object participates in a strand that completes the chain.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.chain_graphs.individual_strand_access_interval_graph`
              - Create an interval graph of the time intervals for each strand in a Chain that completes the chain.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.chain_graphs.number_of_accesses_line_chart`
              - Create a plot of the number of objects participating in a strand that completes the chain at the given time, as a function of time.

Description
-----------

Provides graphs for Chain objects.

.. py:currentmodule:: ansys.stk.extensions.data_analysis.graphs.chain_graphs

.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     angle_between_line_chart<chain_graphs/angle_between_line_chart>
     bentpipe_link_cno_line_chart<chain_graphs/bentpipe_link_cno_line_chart>
     complete_chain_access_interval_graph<chain_graphs/complete_chain_access_interval_graph>
     individual_object_access_interval_graph<chain_graphs/individual_object_access_interval_graph>
     individual_strand_access_interval_graph<chain_graphs/individual_strand_access_interval_graph>
     number_of_accesses_line_chart<chain_graphs/number_of_accesses_line_chart>
