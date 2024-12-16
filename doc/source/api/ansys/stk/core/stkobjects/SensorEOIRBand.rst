SensorEOIRBand
==============

.. py:class:: ansys.stk.core.stkobjects.SensorEOIRBand

   Class defining an EOIR band.

.. py:currentmodule:: SensorEOIRBand

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.band_name`
              - Gets or sets the name of the band.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.render_band`
              - Band render flag.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.calculating_parameters`
              - Flag to set if input parameters are currently being calculated and entered into the object model.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.horizontal_half_angle`
              - Half the horizontal angular extent of the rectangular EOIR sensor bands field-of-view.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.vertical_half_angle`
              - Half the vertical angular extent of the rectangular EOIR sensor bands field-of-view.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.horizontal_pixels`
              - Gets or sets the number of pixels or samples distributed evenly across the horizontal dimension of the rectangular EOIR sensor bands focal plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.number_of_vertical_pixels`
              - Gets or sets the number of pixels or samples distributed evenly across the vertical dimension of the rectangular EOIR sensor bands focal plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.horizontal_pixel_spacing`
              - Gets or sets the spacing between pixels or samples along the horizontal dimension of the rectangular EOIR sensor bands focal plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.vertical_pixel_spacing`
              - Gets or sets the spacing between pixels or samples along the vertical dimension of the rectangular EOIR sensor bands focal plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.horizontal_individual_field_of_view`
              - Get the horizontal angular extent of a single individual pixels field-of-view for this sensor band.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.vertical_extent_of_individual_pixel_field_of_view`
              - Get the vertical angular extent of a single individual pixels field-of-view for this sensor band.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.low_band_edge_wavelength`
              - Gets or sets the cut-on spectral wavelength of the current sensor band at least one nanometer less than the cut-off value.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.high_band_edge_wavelength`
              - Gets or sets the cut-off spectral wavelength of the current sensor band at least one nanometer greater than the cut-on value.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.number_of_intervals`
              - Gets or sets the number of oversampled spectral intervals to discretely simulate for this sensor band.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.f_number`
              - Gets or sets the F-Number ratio of the system, the effective focal length divided by the clear aperture diameter for this sensor band.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.long_d_focus`
              - Gets or sets the amount of defocus along the optical axis between the ideal image focal plane and the actual detector focal plane for the current sensor band.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.effective_focal_length`
              - Gets or sets the effective focal length of the current sensor band.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.image_quality`
              - Discrete level of optical image quality. Aberrations are modeled based on a RMS wavefront error.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.entrance_prescription_diameter`
              - Diameter of the single lens equivalent optical prescription.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.wavelength`
              - Gets or sets the wavelength in the sensors spectral band to use for diffraction modeling calculations.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.wavelength_type`
              - Gets or sets the relative position within the sensors spectral band to use as the reference wavelength for diffraction modeling calculations.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.integration_time`
              - Gets or sets the time interval over which radiant signal is collected before generating an image.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.saturation_mode`
              - Gets or sets the radiant energy units for saturation and sensitivity, Irradiance better suited for observing point sources or Radiance better suited for resolved images.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.dynamic_range`
              - Get the ratio of the brightest signal to the noise floor.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.dynamic_range_mode`
              - Unlimited allowing pixels to measure any amount of radiant signal without limit or Simulate Saturation where pixels can only measure up to the specified saturation level of radiant signal.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.noise_equivalent_irradiance`
              - Noise equivalent irradiance or radiance for the current sensor band.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.saturation_equivalent_irradiance`
              - Saturation equivalent irradiance or radiance for the current sensor band.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.sensitivities`
              - Get the collection of Sensitivity time-value pairs.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.saturations`
              - Get the collection of Saturation time-value pairs.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.spatial_input_mode`
              - Spatial parameter input mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.spectral_shape`
              - Overall system spectral shape designation.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.system_relative_spectral_response_filename`
              - System relative spectral response file.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.rsr_units`
              - System custom RSR units.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.optical_input_mode`
              - Optical parameter input mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.root_mean_squared_wavefront_error`
              - Gets or sets the RMS wavefront error of the optical system.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.optical_quality_data_filename`
              - Optical quality describing data file.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.optical_transmission_mode`
              - Optical transmission input mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.optical_transmission`
              - Band effective optical transmission.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.optical_transmission_spectral_response_filename`
              - Optical spectral transmission data file.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.optical_quality_data_file_spatial_sampling`
              - Optical quality data file spatial sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.optical_quality_data_file_frequency_sampling`
              - Optical quality data file frequency sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.radiometric_parameter_level`
              - Radiometric parameter input level.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.simulate_quantization`
              - Simulate quantization effects of the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.quantum_efficiency_mode`
              - Quantum efficiency input mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.quantization_mode`
              - Quantization input mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.quantum_efficiency_value`
              - Band effective detector quantum efficiency.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.detector_fill_factor`
              - Gets or sets the effective fill factor of photosensitive surface area to the total detector surface area.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.read_noise`
              - Gets or sets the read noise from the detectors in electrons.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.dark_current`
              - Gets or sets the dark current noise rate from the detectors in electrons-per-second-per-detector.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.detector_full_well_capacity`
              - Gets or sets the full-well capacity of the detectors in electrons-per-detector.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.bit_depth`
              - Gets or sets the number of bits to encode the digital signal with.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.quantization_step_size`
              - Gets or sets the quantization step size of the digital output signal.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.quantum_efficiency_filename`
              - Spectral quantum efficiency data file for the detectors.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.spatial_auto_rebalance`
              - Spatial parameter auto rebalance.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBand.optical_automatic_rebalance`
              - Spatial parameter auto rebalance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorEOIRBand


Property detail
---------------

.. py:property:: band_name
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.band_name
    :type: str

    Gets or sets the name of the band.

.. py:property:: render_band
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.render_band
    :type: bool

    Band render flag.

.. py:property:: calculating_parameters
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.calculating_parameters
    :type: bool

    Flag to set if input parameters are currently being calculated and entered into the object model.

.. py:property:: horizontal_half_angle
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.horizontal_half_angle
    :type: typing.Any

    Half the horizontal angular extent of the rectangular EOIR sensor bands field-of-view.

.. py:property:: vertical_half_angle
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.vertical_half_angle
    :type: typing.Any

    Half the vertical angular extent of the rectangular EOIR sensor bands field-of-view.

.. py:property:: horizontal_pixels
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.horizontal_pixels
    :type: float

    Gets or sets the number of pixels or samples distributed evenly across the horizontal dimension of the rectangular EOIR sensor bands focal plane.

.. py:property:: number_of_vertical_pixels
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.number_of_vertical_pixels
    :type: float

    Gets or sets the number of pixels or samples distributed evenly across the vertical dimension of the rectangular EOIR sensor bands focal plane.

.. py:property:: horizontal_pixel_spacing
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.horizontal_pixel_spacing
    :type: float

    Gets or sets the spacing between pixels or samples along the horizontal dimension of the rectangular EOIR sensor bands focal plane.

.. py:property:: vertical_pixel_spacing
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.vertical_pixel_spacing
    :type: float

    Gets or sets the spacing between pixels or samples along the vertical dimension of the rectangular EOIR sensor bands focal plane.

.. py:property:: horizontal_individual_field_of_view
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.horizontal_individual_field_of_view
    :type: float

    Get the horizontal angular extent of a single individual pixels field-of-view for this sensor band.

.. py:property:: vertical_extent_of_individual_pixel_field_of_view
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.vertical_extent_of_individual_pixel_field_of_view
    :type: float

    Get the vertical angular extent of a single individual pixels field-of-view for this sensor band.

.. py:property:: low_band_edge_wavelength
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.low_band_edge_wavelength
    :type: float

    Gets or sets the cut-on spectral wavelength of the current sensor band at least one nanometer less than the cut-off value.

.. py:property:: high_band_edge_wavelength
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.high_band_edge_wavelength
    :type: float

    Gets or sets the cut-off spectral wavelength of the current sensor band at least one nanometer greater than the cut-on value.

.. py:property:: number_of_intervals
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.number_of_intervals
    :type: int

    Gets or sets the number of oversampled spectral intervals to discretely simulate for this sensor band.

.. py:property:: f_number
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.f_number
    :type: float

    Gets or sets the F-Number ratio of the system, the effective focal length divided by the clear aperture diameter for this sensor band.

.. py:property:: long_d_focus
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.long_d_focus
    :type: float

    Gets or sets the amount of defocus along the optical axis between the ideal image focal plane and the actual detector focal plane for the current sensor band.

.. py:property:: effective_focal_length
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.effective_focal_length
    :type: float

    Gets or sets the effective focal length of the current sensor band.

.. py:property:: image_quality
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.image_quality
    :type: SensorEOIRBandImageQuality

    Discrete level of optical image quality. Aberrations are modeled based on a RMS wavefront error.

.. py:property:: entrance_prescription_diameter
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.entrance_prescription_diameter
    :type: float

    Diameter of the single lens equivalent optical prescription.

.. py:property:: wavelength
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.wavelength
    :type: float

    Gets or sets the wavelength in the sensors spectral band to use for diffraction modeling calculations.

.. py:property:: wavelength_type
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.wavelength_type
    :type: SensorEOIRBandWavelengthType

    Gets or sets the relative position within the sensors spectral band to use as the reference wavelength for diffraction modeling calculations.

.. py:property:: integration_time
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.integration_time
    :type: float

    Gets or sets the time interval over which radiant signal is collected before generating an image.

.. py:property:: saturation_mode
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.saturation_mode
    :type: SensorEOIRBandSaturationMode

    Gets or sets the radiant energy units for saturation and sensitivity, Irradiance better suited for observing point sources or Radiance better suited for resolved images.

.. py:property:: dynamic_range
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.dynamic_range
    :type: float

    Get the ratio of the brightest signal to the noise floor.

.. py:property:: dynamic_range_mode
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.dynamic_range_mode
    :type: bool

    Unlimited allowing pixels to measure any amount of radiant signal without limit or Simulate Saturation where pixels can only measure up to the specified saturation level of radiant signal.

.. py:property:: noise_equivalent_irradiance
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.noise_equivalent_irradiance
    :type: float

    Noise equivalent irradiance or radiance for the current sensor band.

.. py:property:: saturation_equivalent_irradiance
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.saturation_equivalent_irradiance
    :type: float

    Saturation equivalent irradiance or radiance for the current sensor band.

.. py:property:: sensitivities
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.sensitivities
    :type: SensorEOIRSensitivityCollection

    Get the collection of Sensitivity time-value pairs.

.. py:property:: saturations
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.saturations
    :type: SensorEOIRSaturationCollection

    Get the collection of Saturation time-value pairs.

.. py:property:: spatial_input_mode
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.spatial_input_mode
    :type: SensorEOIRBandSpatialInputMode

    Spatial parameter input mode.

.. py:property:: spectral_shape
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.spectral_shape
    :type: SensorEOIRBandSpectralShape

    Overall system spectral shape designation.

.. py:property:: system_relative_spectral_response_filename
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.system_relative_spectral_response_filename
    :type: str

    System relative spectral response file.

.. py:property:: rsr_units
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.rsr_units
    :type: SensorEOIRBandSpectralRelativeSystemResponseUnitsType

    System custom RSR units.

.. py:property:: optical_input_mode
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.optical_input_mode
    :type: SensorEOIRBandOpticalInputMode

    Optical parameter input mode.

.. py:property:: root_mean_squared_wavefront_error
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.root_mean_squared_wavefront_error
    :type: float

    Gets or sets the RMS wavefront error of the optical system.

.. py:property:: optical_quality_data_filename
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.optical_quality_data_filename
    :type: str

    Optical quality describing data file.

.. py:property:: optical_transmission_mode
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.optical_transmission_mode
    :type: SensorEOIRBandOpticalTransmissionMode

    Optical transmission input mode.

.. py:property:: optical_transmission
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.optical_transmission
    :type: float

    Band effective optical transmission.

.. py:property:: optical_transmission_spectral_response_filename
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.optical_transmission_spectral_response_filename
    :type: str

    Optical spectral transmission data file.

.. py:property:: optical_quality_data_file_spatial_sampling
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.optical_quality_data_file_spatial_sampling
    :type: float

    Optical quality data file spatial sampling.

.. py:property:: optical_quality_data_file_frequency_sampling
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.optical_quality_data_file_frequency_sampling
    :type: float

    Optical quality data file frequency sampling.

.. py:property:: radiometric_parameter_level
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.radiometric_parameter_level
    :type: SensorEOIRBandRadiometricParameterLevelType

    Radiometric parameter input level.

.. py:property:: simulate_quantization
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.simulate_quantization
    :type: bool

    Simulate quantization effects of the sensor.

.. py:property:: quantum_efficiency_mode
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.quantum_efficiency_mode
    :type: SensorEOIRBandQuantumEfficiencyMode

    Quantum efficiency input mode.

.. py:property:: quantization_mode
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.quantization_mode
    :type: SensorEOIRBandQuantizationMode

    Quantization input mode.

.. py:property:: quantum_efficiency_value
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.quantum_efficiency_value
    :type: float

    Band effective detector quantum efficiency.

.. py:property:: detector_fill_factor
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.detector_fill_factor
    :type: float

    Gets or sets the effective fill factor of photosensitive surface area to the total detector surface area.

.. py:property:: read_noise
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.read_noise
    :type: float

    Gets or sets the read noise from the detectors in electrons.

.. py:property:: dark_current
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.dark_current
    :type: float

    Gets or sets the dark current noise rate from the detectors in electrons-per-second-per-detector.

.. py:property:: detector_full_well_capacity
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.detector_full_well_capacity
    :type: float

    Gets or sets the full-well capacity of the detectors in electrons-per-detector.

.. py:property:: bit_depth
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.bit_depth
    :type: int

    Gets or sets the number of bits to encode the digital signal with.

.. py:property:: quantization_step_size
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.quantization_step_size
    :type: float

    Gets or sets the quantization step size of the digital output signal.

.. py:property:: quantum_efficiency_filename
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.quantum_efficiency_filename
    :type: str

    Spectral quantum efficiency data file for the detectors.

.. py:property:: spatial_auto_rebalance
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.spatial_auto_rebalance
    :type: bool

    Spatial parameter auto rebalance.

.. py:property:: optical_automatic_rebalance
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBand.optical_automatic_rebalance
    :type: bool

    Spatial parameter auto rebalance.


