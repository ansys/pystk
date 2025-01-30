FigureOfMeritConstraintName
===========================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritConstraintName

   IntEnum


.. py:currentmodule:: FigureOfMeritConstraintName

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown constraint.

            * - :py:attr:`~ALTITUDE`
              - Altitude constraint.

            * - :py:attr:`~ANGULAR_RATE`
              - Angular Rate constraint.

            * - :py:attr:`~APPARENT_TIME`
              - Apparent Time constraint.

            * - :py:attr:`~AZIMUTH_ANGLE`
              - Azimuth Angle constraint.

            * - :py:attr:`~AZIMUTH_RATE`
              - Azimuth Rate constraint.

            * - :py:attr:`~CENTRAL_BODY_OBSTRUCTION`
              - Central Body Obstruction constraint.

            * - :py:attr:`~VECTOR_GEOMETRY_TOOL_ANGLE`
              - Angle constraint.

            * - :py:attr:`~VECTOR_MAGNITUDE`
              - Vector Magnitude constraint.

            * - :py:attr:`~ELEVATION_ANGLE`
              - Elevation Angle constraint.

            * - :py:attr:`~ELEVATION_RATE`
              - Elevation Rate constraint.

            * - :py:attr:`~ELEVATION_RISE_SET`
              - Elevation Rise Set constraint.

            * - :py:attr:`~GEO_EXCLUSION`
              - Geo Exclusion constraint.

            * - :py:attr:`~GROUND_SAMPLE_DISTANCE`
              - Ground Sample Distance constraint.

            * - :py:attr:`~HEIGHT_ABOVE_HORIZON`
              - Height Above Horizon constraint.

            * - :py:attr:`~LINE_OF_SIGHT_LUNAR_EXCLUSION_ANGLE`
              - LOS Lunar Exclusion constraint.

            * - :py:attr:`~LINE_OF_SIGHT_SOLAR_EXCLUSION_ANGLE`
              - LOS Sun Exclusion constraint.

            * - :py:attr:`~LUNAR_ELEVATION_ANGLE`
              - Lunar Elevation Angle constraint.

            * - :py:attr:`~MATLAB`
              - Matlab constraint.

            * - :py:attr:`~OBJECT_EXCLUSION_ANGLE`
              - Object Exclusion Angle constraint.

            * - :py:attr:`~PROPAGATION_DELAY`
              - Propagation Delay constraint.

            * - :py:attr:`~RANGE`
              - Range constraint.

            * - :py:attr:`~RANGE_RATE`
              - Range Rate constraint.

            * - :py:attr:`~SAR_AREA_RATE`
              - SAR Area Rate constraint.

            * - :py:attr:`~SAR_AZIMUTH_RESOLUTION`
              - SAR Azimuth Resolution constraint.

            * - :py:attr:`~SAR_CARRIER_TO_NOISE_RATIO`
              - SAR Carrier-to-Noise Ratio constraint.

            * - :py:attr:`~SAR_EXTERNAL_DATA`
              - SAR External Data constraint.

            * - :py:attr:`~SAR_INTEGRATION_TIME`
              - SAR Integration Time constraint.

            * - :py:attr:`~SAR_PTCR`
              - SAR Point-Target-to-Clutter Ratio constraint.

            * - :py:attr:`~SAR_SCR`
              - SAR Signal-to-Clutter Ratio constraint.

            * - :py:attr:`~SAR_SNR`
              - SAR Signal-to-Noise Ratio constraint.

            * - :py:attr:`~SAR_SIGMA_N`
              - SAR Sigma N constraint.

            * - :py:attr:`~SEARCH_TRACK_DWELL_TIME`
              - Search-Track Dwell Time constraint.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_PROBABILITY_OF_DETECTION`
              - Search-Track Integrated Probability of Detection constraint.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_SNR`
              - Search-Track Integrated Signal-to-Noise Ratio constraint.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATION_TIME`
              - Search-Track Integration Time constraint.

            * - :py:attr:`~SEARCH_TRACK_SINGLE_PULSE_PROBABILITY_OF_DETECTION`
              - Search-Track Single Pulse Probability of Detection constraint.

            * - :py:attr:`~SEARCH_TRACK_SINGLE_PULSE_SNR`
              - Search-Track Single Pulse Signal-to-Noise Ratio constraint.

            * - :py:attr:`~SUN_ELEVATION_ANGLE`
              - Sun Elevation Angle constraint.

            * - :py:attr:`~TERRAIN_GRAZING_ANGLE`
              - Terrain Grazing Angle constraint.

            * - :py:attr:`~ANGLE_TO_ASSET`
              - Angle To Asset constraint.

            * - :py:attr:`~LINE_OF_SIGHT`
              - Line Of Sight constraint.

            * - :py:attr:`~AZ_EL_MASK`
              - Azimuth Elevation Mask constraint.

            * - :py:attr:`~DURATION`
              - Duration constraint.

            * - :py:attr:`~GMT`
              - Greenwich Mean Time constraint.

            * - :py:attr:`~IMAGE_QUALITY`
              - Image Quality constraint.

            * - :py:attr:`~INTERVALS`
              - Intervals constraint.

            * - :py:attr:`~LIGHTING`
              - Light constraint.

            * - :py:attr:`~LOCAL_TIME`
              - Local Time constraint.

            * - :py:attr:`~LINE_OF_SIGHT_CENTRAL_BODY_EXCLUSION`
              - Loss Of Signal Central Body Exclusion constraint.

            * - :py:attr:`~POINT_METRIC`
              - Coordinate Point Metric constraint.

            * - :py:attr:`~CENTROID_AZIMUTH_ANGLE`
              - Do not use this enumeration, as it is deprecated. Centroid Azimuth Angle constraint.

            * - :py:attr:`~CENTROID_RANGE`
              - Do not use this enumeration, as it is deprecated. Centroid Range constraint.

            * - :py:attr:`~CENTROID_SUN_ELEVATION_ANGLE`
              - Do not use this enumeration, as it is deprecated. Centroid Sun Elevation Angle constraint.

            * - :py:attr:`~COLLECTION_ANGLE`
              - Collection Angle constraint.

            * - :py:attr:`~DOPPLER_CONE_ANGLE`
              - Doppler Cone Angle constraint.

            * - :py:attr:`~LATITUDE`
              - Latitude constraint.

            * - :py:attr:`~SUN_GROUND_ELEVATION_ANGLE`
              - Sun Ground Elevation Angle constraint.

            * - :py:attr:`~TERRAIN_MASK`
              - Terrain Mask constraint.

            * - :py:attr:`~CROSS_TRACK_RANGE`
              - Cross Track Range constraint.

            * - :py:attr:`~IN_TRACK_RANGE`
              - In Track Range constraint.

            * - :py:attr:`~SQUINT_ANGLE`
              - Squinting Angle constraint.

            * - :py:attr:`~BACKGROUND`
              - Background constraint.

            * - :py:attr:`~FOREGROUND`
              - Foreground constraint.

            * - :py:attr:`~BETA_ANGLE`
              - Beta Angle constraint.

            * - :py:attr:`~AREA_TARGET_CENTROID_ELEVATION_ANGLE`
              - Do not use this enumeration, as it is deprecated. Area Target Centroid Elevation Angle constraint.

            * - :py:attr:`~EXCLUSION_ZONE`
              - Exclusion Zone constraint.

            * - :py:attr:`~GRAZING_ANGLE`
              - Grazing Angle constraint.

            * - :py:attr:`~GRAZING_ALTITUDE`
              - Grazing Altitude constraint.

            * - :py:attr:`~GROUND_ELEVATION_ANGLE`
              - Ground Elevation Angle constraint.

            * - :py:attr:`~GROUND_TRACK`
              - Ground Track constraint.

            * - :py:attr:`~INCLUSION_ZONE`
              - Inclusion Zone constraint.

            * - :py:attr:`~SUN_SPECULAR_EXCLUSION`
              - Sun Specular Exclusion constraint.

            * - :py:attr:`~DEPTH`
              - Deptch constraint.

            * - :py:attr:`~FIELD_OF_VIEW`
              - Field Of View constraint.

            * - :py:attr:`~ANGLE_OFF_BORESIGHT`
              - Angle Of Boresight constraint.

            * - :py:attr:`~ANGLE_OFF_BORESIGHT_RATE`
              - Angle Of Boresight Rate constraint.

            * - :py:attr:`~BORESIGHT_GRAZING_ANGLE`
              - Boresight Grazing Angle constraint.

            * - :py:attr:`~BORESIGHT_INTERSECTION_LIGHTING_CONDITION`
              - BS Intersection Light Condition constraint.

            * - :py:attr:`~FIELD_OF_VIEW_SUN_SPECULAR_EXCLUSION`
              - Field Of View Sun Specular Exclusion constraint.

            * - :py:attr:`~FIELD_OF_VIEW_SUN_SPECULAR_INCLUSION`
              - Field Of View Sun Specular Inclusion constraint.

            * - :py:attr:`~HORIZON_CROSSING`
              - Horizon Crossing constraint.

            * - :py:attr:`~BORESIGHT_LUNAR_EXCLUSION_ANGLE`
              - BS Lunar Exclusion constraint.

            * - :py:attr:`~BORESIGHT_SOLAR_EXCLUSION_ANGLE`
              - BS Sun Exclusion constraint.

            * - :py:attr:`~BORESIGHT_CENTRAL_BODY_EXCLUSION_ANGLE`
              - BS Centray Body Exclusion constraint.

            * - :py:attr:`~CENTRAL_BODY_OBSTRUCTION_CROSS_INWARD`
              - Field Of View Central Body Obstruction Cross In constraint.

            * - :py:attr:`~CENTRAL_BODY_OBSTRUCTION_CROSS_OUTWARD`
              - Field Of View Central Body Obstruction Cross Out constraint.

            * - :py:attr:`~CENTRAL_BODY_HORIZON_REFINE`
              - Field Of View Central Body Horizon Refine constraint.

            * - :py:attr:`~CENTRAL_BODY_CENTER`
              - Field Of View Central Body Center constraint.

            * - :py:attr:`~SENSOR_AZ_EL_MASK`
              - Sensor Azimuth Elevation Mask constraint.

            * - :py:attr:`~SENSOR_RANGE_MASK`
              - Sensor Range Mask constraint.

            * - :py:attr:`~INFRARED_DETECTION`
              - Infrared Detection constraint.

            * - :py:attr:`~RADAR_TRANSMITTER_TARGET_ACCESS`
              - Radar Xmt Target Access constraint.

            * - :py:attr:`~RADAR_TRANSMITTER_ACCESS`
              - Radar Xmt Access constraint.

            * - :py:attr:`~RADAR_ACCESS`
              - Radar Access constraint.

            * - :py:attr:`~BISTATIC_ANGLE`
              - Bistatic Angle constraint.

            * - :py:attr:`~NOISE_TEMPERATURE`
              - Noise Temperature constraint.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_PULSES`
              - Search-Track Integrated Pulses constraint.

            * - :py:attr:`~SEARCH_TRACK_MLC_FILTER`
              - Search-Track MLC Filter constraint.

            * - :py:attr:`~SEARCH_TRACK_SLC_FILTER`
              - Search-Track SLC Filter constraint.

            * - :py:attr:`~SEARCH_TRACK_CLEAR_DOPPLER`
              - Search-Track Clear Doppler constraint.

            * - :py:attr:`~SEARCH_TRACK_UNAMBIGUOUS_RANGE`
              - Search-Track Unambiguous Range constraint.

            * - :py:attr:`~SEARCH_TRACK_UNAMBIGUOUS_DOPPLER`
              - Search-Track Unambiguous Doppler constraint.

            * - :py:attr:`~SEARCH_TRACK_SINGLE_PULSE_SNR_JAMMING`
              - Search-Track Single Pulse SNR Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_SINGLE_PULSE_J_OVER_S`
              - Search-Track Single Pulse J/S constraint.

            * - :py:attr:`~SEARCH_TRACK_SINGLE_PULSE_PROBABILITY_OF_DETECTION_JAMMING`
              - Search-Track Single Pulse PDet Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_SNR_JAMMING`
              - Search-Track Integrated SNR Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_J_OVER_S`
              - Search-Track Integrated J/S constraint.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_PROBABILITY_OF_DETECTION_JAMMING`
              - Search-Track Integrated PDet Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_PULSES_JAMMING`
              - Search-Track Integrated Pulses Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATION_TIME_JAMMING`
              - Search-Track Integration Time Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_DWELL_TIME_JAMMING`
              - Search-Track Dwell Time Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_CONSTRAINT_PLUGIN`
              - Search-Track Constraint Plugin constraint.

            * - :py:attr:`~SAR_SNR_JAMMING`
              - SAR SNR Jamming constraint.

            * - :py:attr:`~SAR_CARRIER_TO_NOISE_RATIO_JAMMING`
              - SAR CNR Jamming constraint.

            * - :py:attr:`~SAR_SCR_JAMMING`
              - SAR SCR Jamming constraint.

            * - :py:attr:`~SAR_J_OVER_S`
              - SAR J/S constraint.

            * - :py:attr:`~SAR_CONSTRAINT_PLUGIN`
              - SAR Constraint Plugin constraint.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_SNR`
              - SAR Orthogonal Polar SNR constraint.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_CNR`
              - SAR Orthogonal Polar CNR constraint.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_SCR`
              - SAR Orthogonal Polar SCR constraint.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_PTCR`
              - SAR Orthogonal Polar PTCR constraint.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_SNR_JAMMING`
              - SAR Orthogonal Polar SNR Jamming constraint.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_CNR_JAMMING`
              - SAR Orthogonal Polar CNR Jamming constraint.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_SCR_JAMMING`
              - SAR Orthogonal Polar SCR Jamming constraint.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_J_OVER_S`
              - SAR Orthogonal Polar J/S constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_SNR`
              - Search-Track Orthogonal Polar Single Pulse SNR constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_PROBABILITY_OF_DETECTION`
              - Search-Track Orthogonal Polar Single Pulse PDet constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_SNR`
              - Search-Track Orthogonal Polar Integrated SNR constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PROBABILITY_OF_DETECTION`
              - Search-Track Orthogonal Polar Integrated PDet constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PULSES`
              - Search-Track Orthogonal Polar Integrated Pulses constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATION_TIME`
              - Search-Track Orthogonal Polar Integration Time constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_DWELL_TIME`
              - Search-Track Orthogonal Polar Dwell Time constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_SNR_JAMMING`
              - Search-Track Orthogonal Polar Single Pulse SNR Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_J_OVER_S`
              - Search-Track Orthogonal Polar Single Pulse J/S constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_PROBABILITY_OF_DETECTION_JAMMING`
              - Search-Track Orthogonal Polar Single Pulse PDet Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_SNR_JAMMING`
              - Search-Track Orthogonal Polar Integrated SNR Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_J_OVER_S`
              - Search-Track Orthogonal Polar Integrated J/S constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PROBABILITY_OF_DETECTION_JAMMING`
              - Search-Track Orthogonal Polar Integrated PDet Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PULSES_JAMMING`
              - Search-Track Orthogonal Polar Integrated Pulses Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATION_TIME_JAMMING`
              - Search-Track Orthogonal Polar Integration Time Jamming constraint.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_DWELL_TIME_JAMMING`
              - Search-Track Orthogonal Polar Dwell Time Jamming constraint.

            * - :py:attr:`~FREQUENCY`
              - Frequency constraint.

            * - :py:attr:`~DOPPLER_SHIFT`
              - Doppler Shift constraint.

            * - :py:attr:`~RECEIVED_ISOTROPIC_POWER`
              - Received Isotropic Power constraint.

            * - :py:attr:`~POWER_AT_RECEIVER_INPUT`
              - Power at Receiver Input constraint.

            * - :py:attr:`~FLUX_DENSITY`
              - Flux Density constraint.

            * - :py:attr:`~G_OVER_T`
              - G/T constraint.

            * - :py:attr:`~C_OVER_N0`
              - C/No constraint.

            * - :py:attr:`~C_OVER_N`
              - C/N constraint.

            * - :py:attr:`~LINK_MARGIN`
              - Link Margin constraint.

            * - :py:attr:`~EB_OVER_N0`
              - Energy per bit to noise ratio (Eb/No) constraint.

            * - :py:attr:`~BIT_ERROR_RATE`
              - Bit Error Rate constraint.

            * - :py:attr:`~POLARIZATION_RELATIVE_ANGLE`
              - Polarization Relative Angle constraint.

            * - :py:attr:`~COMM_PLUGIN`
              - Comm Plugin constraint.

            * - :py:attr:`~LINK_EIRP`
              - Link EIRP constraint.

            * - :py:attr:`~POWER_FLUX_DENSITY`
              - Power Flux Density constraint.

            * - :py:attr:`~TOTAL_RECEIVED_REFRACTION_POWER`
              - Total Received Rf Power constraint.

            * - :py:attr:`~C_OVER_N0_PLUS_I0`
              - C/No+Io constraint.

            * - :py:attr:`~C_OVER_N_PLUS_I`
              - C/N+I constraint.

            * - :py:attr:`~C_OVER_I`
              - C/I constraint.

            * - :py:attr:`~J_OVER_S`
              - J/S constraint.

            * - :py:attr:`~DELTA_T_OVER_T`
              - Delta T/T constraint.

            * - :py:attr:`~EB_OVER_N0_PLUS_I0`
              - Eb/No+Io constraint.

            * - :py:attr:`~BER_PLUS_I`
              - BER+I constraint.

            * - :py:attr:`~FREQUENCY_TRACK`
              - Frequency Track constraint.

            * - :py:attr:`~PHASE_TRACK`
              - Phase Track constraint.

            * - :py:attr:`~CODE_TRACK`
              - Code Track constraint.

            * - :py:attr:`~C_OVER_N0_PLUS_I_GPS_CHANNEL`
              - CNoIGPSCh constraint.

            * - :py:attr:`~ACCESS_CONSTRAINT_PLUGIN`
              - Access Constraint Plugin constraint.

            * - :py:attr:`~THIRD_BODY_OBS`
              - Do not use this enumeration, as it is deprecated. Third Body Obstruction constraint.

            * - :py:attr:`~SPECTRAL_FLUX_DENSITY`
              - Spectral Flux Density constraint.

            * - :py:attr:`~CONDITION`
              - Crdn Condition constraint.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritConstraintName


