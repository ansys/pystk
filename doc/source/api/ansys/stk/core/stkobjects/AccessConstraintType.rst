AccessConstraintType
====================

.. py:class:: ansys.stk.core.stkobjects.AccessConstraintType

   IntEnum


.. py:currentmodule:: AccessConstraintType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~NONE`
              - None. Use interface IAgAccessConstraint.

            * - :py:attr:`~IMAGE_QUALITY`
              - Image quality. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~ALTITUDE`
              - Altitude. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~ANGULAR_RATE`
              - Angular rate. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~APPARENT_TIME`
              - Apparent time. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~AREA_TARGET_CENTROID_ELEVATION_ANGLE`
              - Do not use this enumeration, as it is deprecated. Area Target centroid elevation angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~AZIMUTH_ANGLE`
              - Azimuth angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~BACKGROUND`
              - Background. Use interface IAgAccessCnstrBackground.

            * - :py:attr:`~BETA_ANGLE`
              - Beta angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~VECTOR_GEOMETRY_TOOL_ANGLE`
              - Angle. Use interface IAgAccessCnstrCrdnCn.

            * - :py:attr:`~VECTOR_MAGNITUDE`
              - Vector magnitude. Use interface IAgAccessCnstrCrdnCn.

            * - :py:attr:`~CROSS_TRACK_RANGE`
              - Cross-track range. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~DOPPLER_CONE_ANGLE`
              - Doppler cone angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~DURATION`
              - Duration. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~ELEVATION_ANGLE`
              - Elevation angle. Use interface IAgAccessCnstrMinMax,  IAgAccessCnstrAngle.

            * - :py:attr:`~EXCLUSION_ZONE`
              - Exclusion zone. Use interface IAgAccessCnstrExclZonesCollection, IAgAccessCnstrZone.

            * - :py:attr:`~GMT`
              - GMT. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~GRAZING_ALTITUDE`
              - Grazing altitude. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~GRAZING_ANGLE`
              - Grazing angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~GROUND_ELEVATION_ANGLE`
              - Ground elevation angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~GROUND_TRACK`
              - Ground track. Use interface IAgAccessCnstrGroundTrack.

            * - :py:attr:`~INCLUSION_ZONE`
              - Inclusion zone. Use interface IAgAccessCnstrZone.

            * - :py:attr:`~INTERVALS`
              - Intervals. Use interface IAgAccessCnstrIntervals.

            * - :py:attr:`~IN_TRACK_RANGE`
              - In-track range. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~LATITUDE`
              - Latitude. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~LIGHTING`
              - Lighting. Use interface IAgAccessCnstrCondition.

            * - :py:attr:`~LINE_OF_SIGHT`
              - Line of sight. Use interface IAgAccessConstraint.

            * - :py:attr:`~LOCAL_TIME`
              - Local time. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~LIGHT_OF_SIGHT_LUNAR_EXCLUSION_ANGLE`
              - Line of sight lunar exclusion. Use interface IAgAccessCnstrAngle.

            * - :py:attr:`~LIGHT_OF_SIGHT_SOLAR_EXCLUSION_ANGLE`
              - Line of sight sun exclusion. Use interface IAgAccessCnstrAngle.

            * - :py:attr:`~LUNAR_ELEVATION_ANGLE`
              - Lunar elevation angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MATLAB`
              - Matlab. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~OBJECT_EXCLUSION_ANGLE`
              - Object exclusion angle. Use interface IAgAccessCnstrObjExAngle.

            * - :py:attr:`~PROPAGATION_DELAY`
              - Propagation delay. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~RANGE`
              - Range. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~RANGE_RATE`
              - Range rate. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_AREA_RATE`
              - SAR area rate. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_AZIMUTH_RESOLUTION`
              - SAR azimuth resolution. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_CARRIER_TO_NOISE_RATIO`
              - SAR clutter-to-noise ratio. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_EXTERNAL_DATA`
              - SAR external data. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_INTEGRATION_TIME`
              - SAR integration time. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_PTCR`
              - SAR point target-to-clutter ratio. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_SCR`
              - SAR signal-to-clutter ratio. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_SIGMA_N`
              - SAR sigma N. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_SNR`
              - SAR signal-to-noise ratio. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SQUINT_ANGLE`
              - Squint angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_CLEAR_DOPPLER`
              - Search-track clear doppler. Use interface IAgAccessConstraint.

            * - :py:attr:`~SEARCH_TRACK_DWELL_TIME`
              - Search-track dwell time. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_PROBABILITY_OF_DETECTION`
              - Search-track integrated probability of detection. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_PULSES`
              - Search-track integrated pulses. Use interface IAgAccessConstraint.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_SNR`
              - Search-track integrated signal-to-noise ratio. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATION_TIME`
              - Search-track integration time. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_MLC_FILTER`
              - Search-track main lobe clutter filter. Use interface IAgAccessConstraint.

            * - :py:attr:`~SEARCH_TRACK_SINGLE_PULSE_PROBABILITY_OF_DETECTION`
              - Search-track single-pulse probability of detection. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_SINGLE_PULSE_SNR`
              - Search-track single-pulse signal-to-noise ratio. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_SLC_FILTER`
              - Search-track side lobe clutter filter. Use interface IAgAccessConstraint.

            * - :py:attr:`~SEARCH_TRACK_UNAMBIGUOUS_DOPPLER`
              - Search-track unambiguous doppler. Use interface IAgAccessConstraint.

            * - :py:attr:`~SEARCH_TRACK_UNAMBIGUOUS_RANGE`
              - Search-track unambiguous range. Use interface IAgAccessConstraint.

            * - :py:attr:`~SUN_ELEVATION_ANGLE`
              - Sun elevation angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SUN_GROUND_ELEVATION_ANGLE`
              - Sun ground angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SUN_SPECULAR_EXCLUSION_ANGLE`
              - Sun specular exclusion. Use interface IAgAccessCnstrAngle.

            * - :py:attr:`~THIRD_BODY_OBSTRUCTION`
              - Do not use this enumeration, as it is deprecated. Third body obstruction. Use interface IAgAccessCnstrThirdBody.

            * - :py:attr:`~CENTROID_AZIMUTH_ANGLE`
              - Do not use this enumeration, as it is deprecated. Centroid azimuth angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~CENTROID_RANGE`
              - Do not use this enumeration, as it is deprecated. Centroid range. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~CENTROID_SUN_ELEVATION_ANGLE`
              - Do not use this enumeration, as it is deprecated. Centroid sun elevation angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~COLLECTION_ANGLE`
              - Collection angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~TERRAIN_MASK`
              - Terrain mask. Use interface IAgAccessConstraint.

            * - :py:attr:`~AZ_EL_MASK`
              - Azimuth-elevation mask. Use interface IAgAccessConstraint.

            * - :py:attr:`~AZIMUTH_RATE`
              - Azimuth rate. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~ELEVATION_RATE`
              - Elevation rate. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~GEOSYNCHRONOUS_BELT_EXCLUSION_ANGLE`
              - Geostationary belt exclusion. Use interface IAgAccessCnstrAngle.

            * - :py:attr:`~GROUND_SAMPLE_DISTANCE`
              - Ground sample distance. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~HEIGHT_ABOVE_HORIZON`
              - Height above horizon. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~TERRAIN_GRAZING_ANGLE`
              - Terrain grazing angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~ANGLE_OFF_BORESIGHT`
              - Angle off boresight. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~ANGLE_OFF_BORESIGHT_RATE`
              - Angle off boresight rate. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~AREA_MASK`
              - Area mask. Use interface IAgAccessConstraint.

            * - :py:attr:`~BORESIGHT_GRAZING_ANGLE`
              - Boresight grazing angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~BORESIGHT_INTERSECTION_LIGHTING_CONDITION`
              - Boresight Intersection lighting condition. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~BORESIGHT_LUNAR_EXCLUSION_ANGLE`
              - Boresight lunar exclusion. Use interface IAgAccessCnstrAngle.

            * - :py:attr:`~BORESIGHT_SUN_EXCLUSION_ANGLE`
              - Boresight sun exclusion. Use interface IAgAccessCnstrAngle.

            * - :py:attr:`~FIELD_OF_VIEW`
              - Field of view. Use interface IAgAccessConstraint.

            * - :py:attr:`~FIELD_OF_VIEW_SUN_SPECULAR_EXCLUSION_ANGLE`
              - Field of view sun specular exclusion. Use interface IAgAccessConstraint.

            * - :py:attr:`~FIELD_OF_VIEW_SUN_SPECULAR_INCLUSION_ANGLE`
              - Field of view sun specular inclusion. Use interface IAgAccessConstraint.

            * - :py:attr:`~HORIZON_CROSSING`
              - Horizon crossing. Use interface IAgAccessConstraint.

            * - :py:attr:`~SENSOR_AZ_EL_MASK`
              - Sensor azimuth-elevation mask. Use interface IAgAccessConstraint.

            * - :py:attr:`~FOREGROUND`
              - Foreground. Use interface IAgAccessConstraint.

            * - :py:attr:`~CENTRAL_BODY_OBSTRUCTION`
              - Central Body Obstruction. Use interface IAgAccessCnstrCbObstruction.

            * - :py:attr:`~PLUGIN`
              - Access plugin constraint. Use IAgAccessCnstrPluginMinMax.

            * - :py:attr:`~DEPTH`
              - Depth constraint. Use IAgAccessCnstrPluginMinMax.

            * - :py:attr:`~SEET_MAGNETIC_FIELD_L_SHELL`
              - Magnetic Dipole L-Shell. The L value is a measure to indicate a particle's drift shell in a dipole-approximated magnetic field. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEET_MAGNETIC_FIELD_LINE_SEPARATION`
              - Magnetic Field Line Separation; the centric angle between the North footprint of the field line containing the vehicle's location and the North footprint of the field line containing the target's location. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEET_IMPACT_FLUX`
              - Impact Flux; the total impact flux from all types of meteoroid particles. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEET_DAMAGE_FLUX`
              - Damage Flux; the total impact flux from all types of meteoroid particles causing damage. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEET_DAMAGE_MASS_FLUX`
              - Damage Mass Flux; the total impact mass flux from all meteoroid particles causing damage. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEET_IMPACT_MASS_FLUX`
              - Impact Mass Flux; the total impact mass flux ffrom all types of meteoroid particles. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEET_SAA_FLUX_INTENSITY`
              - SAA Flux Intensity; SAA Flux Intensity is determined at the vehicle's location and for specified proton-energy flux threshold channel. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEET_VEHICLE_TEMPERATURE`
              - Vehicle Temperature, computed assuming thermal equilibrium. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~CONDITION`
              - Coordinate condition constraint. Use interface IAgAccessCnstrCrdnCn.

            * - :py:attr:`~SAR_CARRIER_TO_NOISE_RATIO_JAMIING`
              - SAR CNR Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_J_OVER_S`
              - SAR J/S constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_CARRIER_TO_NOISE_RATIO`
              - SAR Orthogonal Polar CNR constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_CARRIER_TO_NOISE_RATIO_JAMMING`
              - SAR Orthogonal Polar CNR Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_J_OVER_S`
              - SAR Orthogonal Polar J/S constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_PTCR`
              - SAR Orthogonal Polar PTCR constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_SCR`
              - SAR Orthogonal Polar SCR constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_SCR_JAMMING`
              - SAR Orthogonal Polar SCR Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_SNR`
              - SAR Orthogonal Polar SNR constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_ORTHOGONAL_POLARIZATION_SNR_JAMMING`
              - SAR Orthogonal Polar SNR Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_SCR_JAMMING`
              - SAR SCR Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SAR_SNR_JAMMING`
              - SAR SNR Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_DWELL_TIME_JAMMING`
              - Search-Track Dwell Time Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_J_OVER_S`
              - Search-Track Integrated J/S constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_PROBABILITY_OF_DETECTION_JAMMING`
              - Search-Track Integrated PDet Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_PULSES_JAMMING`
              - Search-Track Integrated Pulses Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATED_SNR_JAMMING`
              - Search-Track Integrated SNR Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_INTEGRATION_TIME_JAMMING`
              - Search-Track Integration Time Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_DWELL_TIME`
              - Search-Track Orthogonal Polar Dwell Time constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_DWELL_TIME_JAMMING`
              - Search-Track Orthogonal Polar Dwell Time Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_J_OVER_S`
              - Search-Track Orthogonal Polar Integrated J/S constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PROBABILITY_OF_DETECTION`
              - Search-Track Orthogonal Polar Integrated PDet constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PROBABILITY_OF_DETECTION_JAMMING`
              - Search-Track Orthogonal Polar Integrated PDet Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PULSES`
              - Search-Track Orthogonal Polar Integrated Pulses constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PULSES_JAMMING`
              - Search-Track Orthogonal Polar Integrated Pulses Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_SNR`
              - Search-Track Orthogonal Polar Integrated SNR constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_SNR_JAMMING`
              - Search-Track Orthogonal Polar Integrated SNR Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATION_TIME`
              - Search-Track Orthogonal Polar Integration Time constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATION_TIME_JAMMING`
              - Search-Track Orthogonal Polar Integration Time Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_J_OVER_S`
              - Search-Track Orthogonal Polar Single Pulse J/S constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_PROBABILITY_OF_DETECTION`
              - Search-Track Orthogonal Polar Single Pulse PDet constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_PROBABILITY_OF_DETECTION_JAMMING`
              - Search-Track Orthogonal Polar Single Pulse PDet Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_SNR`
              - Search-Track Orthogonal Polar Single Pulse SNR constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_SNR_JAMMING`
              - Search-Track Orthogonal Polar Integrated SNR Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_SINGLE_PULSE_J_OVER_S`
              - Search-Track Single Pulse J/S constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_SINGLE_PULSE_PROBABILITY_OF_DETECTION_JAMMING`
              - Search-Track Single Pulse PDet Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~SEARCH_TRACK_SINGLE_PULSE_SNR_JAMMING`
              - Search-Track Single Pulse SNR Jamming constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~EOIR_SNR`
              - EOIR SNR constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~FIELD_OF_VIEW_CENTRAL_BODY_CENTER`
              - Field Of View Central Body Center constraint. Use IAgAccessConstraint.

            * - :py:attr:`~FIELD_OF_VIEW_CENTRAL_BODY_HORIZON_REFINE`
              - Field Of View Central Body Horizon Refine constraint. Use IAgAccessConstraint.

            * - :py:attr:`~FIELD_OF_VIEW_CENTRAL_BODY_OBSTRUCTION_CROSSSING_INWARD`
              - Field Of View Central Body Obstruction Cross In constraint. Use IAgAccessConstraint.

            * - :py:attr:`~FIELD_OF_VIEW_CENTRAL_BODY_OBSTRUCTION_CROSSING_OUTWARD`
              - Field Of View Central Body Obstruction Cross Out constraint. Use IAgAccessConstraint.

            * - :py:attr:`~SENSOR_RANGE_MASK`
              - Sensor Range Mask constraint. Use IAgAccessConstraint.

            * - :py:attr:`~ATMOSPHERIC_LOSS`
              - Atmosphere Absorption Loss constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~BER_PLUS_I`
              - BER+I constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~BIT_ERROR_RATE`
              - Bit Error Rate constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~C_OVER_I`
              - C/I constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~C_OVER_N`
              - C/N constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~C_OVER_N_PLUS_I`
              - C/N+I constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~C_OVER_N0`
              - C/No constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~C_OVER_N0_PLUS_I0`
              - C/No+Io constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~CLOUDS_FOG_LOSS`
              - Clouds And Fog Loss constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~COMM_PLUGIN`
              - Comm Plugin constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~DELTA_T_OVER_T`
              - Delta T/T constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~DOPPLER_SHIFT`
              - Doppler Shift constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~EB_OVER_N0`
              - Energy per bit to noise ratio (Eb/No) constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~EB_OVER_N0_PLUS_I0`
              - Eb/No+Io constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~FLUX_DENSITY`
              - Flux Density constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~FREQUENCY`
              - Frequency constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~G_OVER_T`
              - G/T constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~J_OVER_S`
              - J/S constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~LINK_EIRP`
              - Link EIRP constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~LINK_MARGIN`
              - Link Margin constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~NOISE_TEMPERATURE`
              - Noise Temperature constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~POLARIZATION_RELATIVE_ANGLE`
              - Polarization Relative Angle constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~POWER_AT_RECEIVER_INPUT`
              - Power at Receiver Input constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~POWER_FLUX_DENSITY`
              - Power Flux Density constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~RAIN_LOSS`
              - Rain Loss constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~RECEIVED_ISOTROPIC_POWER`
              - Received Isotropic Power constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~USER_CUSTOM_A_LOSS`
              - User Custom A Loss constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~USER_CUSTOM_B_LOSS`
              - User Custom B Loss constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~USER_CUSTOM_C_LOSS`
              - User Custom C Loss constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~FREE_SPACE_LOSS`
              - Free Space Loss constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~PROPAGATION_LOSS`
              - Propagation Loss constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~TOTAL_POWER_AT_RECEIVER_INPUT`
              - Total Power At Receiver Input constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~TOTAL_RECEIVED_REFRACTION_POWER`
              - Total Received Rf Power constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~TROPOSPHERIC_SCINTILLATION_LOSS`
              - Troposphere Scintillation Loss constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~URBAN_TERRES_LOSS`
              - Urban Terrestrial Loss constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~TIME_SLIP_SURFACE_RANGE`
              - Time Slip Surface Range constraint. Use IAgAccessConstraint.

            * - :py:attr:`~CABLE_TRANSFORMATION_DELAY`
              - Cable Transmission Delay constraint. Use IAgAccessCnstrIntervals.

            * - :py:attr:`~PROCESS_DELAY`
              - Process Delay constraint. Use IAgAccessCnstrIntervals.

            * - :py:attr:`~RADAR_TRANSMITTER_TARGET_ACCESS`
              - RdrXmtTgtAccess constraint. Use IAgAccessCnstrIntervals.

            * - :py:attr:`~SUN_ILLUMINATION_ANGLE`
              - Sun Illumination angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~SPECTRAL_FLUX_DENSITY`
              - Spectral Flux Density constraint. Use IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_SINGLE_PULSE_SNR_MINIMUM`
              - Multifunction radar single pulse signal-to-noise ratio minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_SINGLE_PULSE_SNR_MAXIMUM`
              - Multifunction radar single pulse signal-to-noise ratio maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_SINGLE_PULSE_PROBABILITY_OF_DETECTION_MINIMUM`
              - Multifunction radar single pulse probability of detection minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_SINGLE_PULSE_PROBABILITY_OF_DETECTION_MAXIMUM`
              - Multifunction radar single pulse probability of detection maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_SNR_MINIMUM`
              - Multifunction radar integrated signal-to-noise ratio minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_SNR_MAXIMUM`
              - Multifunction radar integrated signal-to-noise ratio maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_PROBABILITY_OF_DETECTION_MINIMUM`
              - Multifunction radar integrated probability of detection minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_PROBABILITY_OF_DETECTION_MAXIMUM`
              - Multifunction radar integrated probability of detection maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_PULSES_MINIMUM`
              - Multifunction radar integrated pulses minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_PULSES_MAXIMUM`
              - Multifunction radar integrated pulses maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_PULSES_JAMMING_MINIMUM`
              - Multifunction radar integrated pulses jamming minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_PULSES_JAMMING_MAXIMUM`
              - Multifunction radar integrated pulses jamming maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATION_TIME_MINIMUM`
              - Multifunction radar integration time minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATION_TIME_MAXIMUM`
              - Multifunction radar integration time maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATION_TIME_JAMMING_MINIMUM`
              - Multifunction radar integration time jamming minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATION_TIME_JAMMING_MAXIMUM`
              - Multifunction radar integration time jamming maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_DWELL_TIME_MINIMUM`
              - Multifunction radar dwell time minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_DWELL_TIME_MAXIMUM`
              - Multifunction radar dwell time maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_DWELL_TIME_JAMMING_MIN`
              - Multifunction radar dwell time jamming minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_DWELL_TIME_JAMMING_MAXIMUM`
              - Multifunction radar dwell time jamming maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_SINGLE_PULSE_J_OVER_S_MINIMUM`
              - Multifunction radar single pulse J/S minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_SINGLE_PULSE_J_OVER_S_MAXIMUM`
              - Multifunction radar single pulse J/S maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_J_OVER_S_MINIMUM`
              - Multifunction radar integrated J/S minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_J_OVER_S_MAXIMUM`
              - Multifunction radar integrated J/S maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_SINGLE_PULSE_SNR_JAMMING_MINIMUM`
              - Multifunction radar single pulse signal-to-noise ratio jamming minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_SINGLE_PULSE_SNR_JAMMING_MAXIMUM`
              - Multifunction radar single pulse signal-to-noise ratio jamming maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_SNR_JAMMING_MINIMUM`
              - Multifunction radar integrated signal-to-noise ratio jamming minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_SNR_JAMMING_MAXIMUM`
              - Multifunction radar integrated signal-to-noise ratio jamming maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_SINGLE_PULSE_PROBABILITY_OF_DETECTION_JAMMING_MINIMUM`
              - Multifunction radar single pulse probability of detection jamming minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_SINGLE_PULSE_PROBABILITY_OF_DETECTION_JAMMING_MAXIMUM`
              - Multifunction radar single pulse probability of detection jamming maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_PROBABILITY_OF_DETECTION_JAMMING_MINIMUM`
              - Multifunction radar integrated probability of detection jamming minimum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~MFR_INTEGRATED_PROBABILITY_OF_DETECTION_JAMMING_MAXIMUM`
              - Multifunction radar integrated probability of detection jamming maximum across all available beams. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~TILES_MASK_3D`
              - 3DTiles mask. Use interface IAgAccessConstraint.

            * - :py:attr:`~CENTRAL_ANGLE`
              - Central angle. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~CENTRAL_DISTANCE`
              - Central distance. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~DISTANCE_FROM_AREA_TARGET_BOUNDARY`
              - Distance from AreaTarget boundary. Measured along the surface from subPoint to closest point of the boundary. The value is signed: if subPoint is inside the boundary, value is negative else positive. Use interface IAgAccessCnstrMinMax.

            * - :py:attr:`~CALCULATION_SCALAR`
              - Scalar Calculation (Calc Scalar). Use interface IAgAccessCnstrCrdnCn.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessConstraintType


