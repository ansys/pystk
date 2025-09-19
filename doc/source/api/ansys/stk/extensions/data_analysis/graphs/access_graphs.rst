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
              - Create a pie chart of the durations of the access intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.access_interval_graph`
              - Create an interval graph of the access intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.aer_line_chart`
              - Create a plot of the azimuth, elevation, and range values for the relative position vector between the base object and the target object, during access intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.angular_rates_line_chart`
              - Create a plot of the azimuth rate, elevation rate, and angular rate over time, during each access interval, from the perspective of the selected object in the Access Tool.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.az_el_polar_center_90_graph`
              - Create a polar plot with elevation as radius and azimuth as angle theta over time, during access intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.bit_error_rate_line_chart`
              - Plot the bit error rate (BER) over time, during each access interval.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.carrier_to_noise_ratio_line_chart`
              - Plot the carrier to noise ratio (C/N) over time, during each access interval.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.cumulative_dwell_cumulative_pie_chart`
              - Graph access interval durations as a cumulative pie chart.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.ebno_line_chart`
              - Plot the energy per bit to noise ratio (Eb/No) over time, during each access interval.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.elevation_angle_line_chart`
              - Create a plot of the elevation angle and its rate over time, during each access interval, from the perspective of the selected object in the Access Tool.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.gaps_interval_graph`
              - Create an interval graph of the intervals where access does not exist between the objects.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.probability_of_detection_line_chart`
              - Graph the probability of a radar pulse search detection versus time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.radar_antenna_gain_line_chart`
              - Graph the antenna gain (value toward the Az, El direction)for both receiver and transmitter versus time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.radar_propagation_loss_line_chart`
              - Graph the receive and transmit total propagation attenuation values for the primary polarization signal channel versus time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.radar_sar_azimuth_resolution_line_chart`
              - Graph the radar SAR azimuth resolution and SAR integration time versus time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.radar_sar_time_resolution_line_chart`
              - Graph the time-varying data for the SAR time-resolution product.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.radar_searchtrack_integration_line_chart`
              - Graph time-varying data for the following radar SearchTrack parameters: S/T integration time, S/T dwell time, and S/T pulses integrated.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.radar_searchtrack_snr_line_chart`
              - Graph radar SearchTrack signal-to-noise ratio versus time.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.radar_system_noise_line_chart`
              - Graph the antenna noise temperature and total noise temperature versus time for a radar receiver.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.revisit_diagram_interval_pie_chart`
              - Create a pie chart showing the durations of access intervals and access gap intervals.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.signal_to_noise_ratio_line_chart`
              - Plot the search track signal to noise ratio (S/N) over time, during each access interval.

            * - :py:func:`~ansys.stk.extensions.data_analysis.graphs.access_graphs.sun_rfi_line_chart`
              - Graph the sun-induced antenna noise temperature as well as the receiver gain to system temperature ratio at the receiver as a function of time.

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
     angular_rates_line_chart<access_graphs/angular_rates_line_chart>
     az_el_polar_center_90_graph<access_graphs/az_el_polar_center_90_graph>
     bit_error_rate_line_chart<access_graphs/bit_error_rate_line_chart>
     carrier_to_noise_ratio_line_chart<access_graphs/carrier_to_noise_ratio_line_chart>
     cumulative_dwell_cumulative_pie_chart<access_graphs/cumulative_dwell_cumulative_pie_chart>
     ebno_line_chart<access_graphs/ebno_line_chart>
     elevation_angle_line_chart<access_graphs/elevation_angle_line_chart>
     gaps_interval_graph<access_graphs/gaps_interval_graph>
     probability_of_detection_line_chart<access_graphs/probability_of_detection_line_chart>
     radar_antenna_gain_line_chart<access_graphs/radar_antenna_gain_line_chart>
     radar_propagation_loss_line_chart<access_graphs/radar_propagation_loss_line_chart>
     radar_sar_azimuth_resolution_line_chart<access_graphs/radar_sar_azimuth_resolution_line_chart>
     radar_sar_time_resolution_line_chart<access_graphs/radar_sar_time_resolution_line_chart>
     radar_searchtrack_integration_line_chart<access_graphs/radar_searchtrack_integration_line_chart>
     radar_searchtrack_snr_line_chart<access_graphs/radar_searchtrack_snr_line_chart>
     radar_system_noise_line_chart<access_graphs/radar_system_noise_line_chart>
     revisit_diagram_interval_pie_chart<access_graphs/revisit_diagram_interval_pie_chart>
     signal_to_noise_ratio_line_chart<access_graphs/signal_to_noise_ratio_line_chart>
     sun_rfi_line_chart<access_graphs/sun_rfi_line_chart>
