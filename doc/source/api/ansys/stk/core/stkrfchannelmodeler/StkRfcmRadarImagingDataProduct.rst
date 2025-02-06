StkRfcmRadarImagingDataProduct
==============================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct

   Imaging data product that facilitates the generation of range doppler radar images.

.. py:currentmodule:: StkRfcmRadarImagingDataProduct

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.name`
              - Gets the image product name.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.enable_sensor_fixed_distance`
              - Enables or disables the fixed disatance mode.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.desired_sensor_fixed_distance`
              - Gets or sets the fixed disatance.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.distance_to_range_window_start`
              - Gets or sets the distance to the range window start.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.distance_to_range_window_center`
              - Gets or sets the distance to the range window center.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.center_image_in_range_window`
              - Enables or disables whether the image will be centered in the range window.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.enable_range_doppler_imaging`
              - Enables radar range-doppler imaging.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.range_pixel_count`
              - Gets or sets the range pixel count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.velocity_pixel_count`
              - Gets or sets the velocity pixel count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.range_window_type`
              - Gets or sets the range window type.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.range_window_side_lobe_level`
              - Gets or sets the range window side lobe level.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.velocity_window_type`
              - Gets or sets the velocity window type.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.velocity_window_side_lobe_level`
              - Gets or sets the velocity window side lobe level.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.range_resolution`
              - Gets or sets the range resolution.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.range_window_size`
              - Gets or sets the range window size.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.cross_range_resolution`
              - Gets or sets the cross range resolution.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.cross_range_window_size`
              - Gets or sets the cross range window size.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.required_bandwidth`
              - Gets the waveform product's required bandwidth.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.collection_angle`
              - Gets the waveform collection angle.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.frequency_samples_per_pulse`
              - Gets the number of frequency samples per pulse.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.minimum_pulse_count`
              - Gets the minimum pulse count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.identifier`
              - Gets the unique identifier for the data product



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import StkRfcmRadarImagingDataProduct


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.name
    :type: str

    Gets the image product name.

.. py:property:: enable_sensor_fixed_distance
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.enable_sensor_fixed_distance
    :type: bool

    Enables or disables the fixed disatance mode.

.. py:property:: desired_sensor_fixed_distance
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.desired_sensor_fixed_distance
    :type: float

    Gets or sets the fixed disatance.

.. py:property:: distance_to_range_window_start
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.distance_to_range_window_start
    :type: float

    Gets or sets the distance to the range window start.

.. py:property:: distance_to_range_window_center
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.distance_to_range_window_center
    :type: float

    Gets or sets the distance to the range window center.

.. py:property:: center_image_in_range_window
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.center_image_in_range_window
    :type: bool

    Enables or disables whether the image will be centered in the range window.

.. py:property:: enable_range_doppler_imaging
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.enable_range_doppler_imaging
    :type: bool

    Enables radar range-doppler imaging.

.. py:property:: range_pixel_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.range_pixel_count
    :type: int

    Gets or sets the range pixel count.

.. py:property:: velocity_pixel_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.velocity_pixel_count
    :type: int

    Gets or sets the velocity pixel count.

.. py:property:: range_window_type
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.range_window_type
    :type: RfcmImageWindowType

    Gets or sets the range window type.

.. py:property:: range_window_side_lobe_level
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.range_window_side_lobe_level
    :type: float

    Gets or sets the range window side lobe level.

.. py:property:: velocity_window_type
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.velocity_window_type
    :type: RfcmImageWindowType

    Gets or sets the velocity window type.

.. py:property:: velocity_window_side_lobe_level
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.velocity_window_side_lobe_level
    :type: float

    Gets or sets the velocity window side lobe level.

.. py:property:: range_resolution
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.range_resolution
    :type: float

    Gets or sets the range resolution.

.. py:property:: range_window_size
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.range_window_size
    :type: float

    Gets or sets the range window size.

.. py:property:: cross_range_resolution
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.cross_range_resolution
    :type: float

    Gets or sets the cross range resolution.

.. py:property:: cross_range_window_size
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.cross_range_window_size
    :type: float

    Gets or sets the cross range window size.

.. py:property:: required_bandwidth
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.required_bandwidth
    :type: float

    Gets the waveform product's required bandwidth.

.. py:property:: collection_angle
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.collection_angle
    :type: float

    Gets the waveform collection angle.

.. py:property:: frequency_samples_per_pulse
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.frequency_samples_per_pulse
    :type: int

    Gets the number of frequency samples per pulse.

.. py:property:: minimum_pulse_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.minimum_pulse_count
    :type: int

    Gets the minimum pulse count.

.. py:property:: identifier
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct.identifier
    :type: str

    Gets the unique identifier for the data product


