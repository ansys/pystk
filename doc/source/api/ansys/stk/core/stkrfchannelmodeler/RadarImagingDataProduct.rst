RadarImagingDataProduct
=======================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct

   Imaging data product that facilitates the generation of range doppler radar images.

.. py:currentmodule:: RadarImagingDataProduct

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.name`
              - Get the image product name.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.enable_sensor_fixed_distance`
              - Enable or disables the fixed disatance mode.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.desired_sensor_fixed_distance`
              - Get or set the fixed disatance.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.distance_to_range_window_start`
              - Get or set the distance to the range window start.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.distance_to_range_window_center`
              - Get or set the distance to the range window center.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.center_image_in_range_window`
              - Enable or disables whether the image will be centered in the range window.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.enable_range_doppler_imaging`
              - Enable radar range-doppler imaging.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.range_pixel_count`
              - Get or set the range pixel count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.velocity_pixel_count`
              - Get or set the velocity pixel count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.range_window_type`
              - Get or set the range window type.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.range_window_side_lobe_level`
              - Get or set the range window side lobe level.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.velocity_window_type`
              - Get or set the velocity window type.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.velocity_window_side_lobe_level`
              - Get or set the velocity window side lobe level.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.range_resolution`
              - Get or set the range resolution.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.range_window_size`
              - Get or set the range window size.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.cross_range_resolution`
              - Get or set the cross range resolution.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.cross_range_window_size`
              - Get or set the cross range window size.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.required_bandwidth`
              - Get the waveform product's required bandwidth.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.collection_angle`
              - Get the waveform collection angle.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.frequency_samples_per_pulse`
              - Get the number of frequency samples per pulse.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.minimum_pulse_count`
              - Get the minimum pulse count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.identifier`
              - Get the unique identifier for the data product



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import RadarImagingDataProduct


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.name
    :type: str

    Get the image product name.

.. py:property:: enable_sensor_fixed_distance
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.enable_sensor_fixed_distance
    :type: bool

    Enable or disables the fixed disatance mode.

.. py:property:: desired_sensor_fixed_distance
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.desired_sensor_fixed_distance
    :type: float

    Get or set the fixed disatance.

.. py:property:: distance_to_range_window_start
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.distance_to_range_window_start
    :type: float

    Get or set the distance to the range window start.

.. py:property:: distance_to_range_window_center
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.distance_to_range_window_center
    :type: float

    Get or set the distance to the range window center.

.. py:property:: center_image_in_range_window
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.center_image_in_range_window
    :type: bool

    Enable or disables whether the image will be centered in the range window.

.. py:property:: enable_range_doppler_imaging
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.enable_range_doppler_imaging
    :type: bool

    Enable radar range-doppler imaging.

.. py:property:: range_pixel_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.range_pixel_count
    :type: int

    Get or set the range pixel count.

.. py:property:: velocity_pixel_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.velocity_pixel_count
    :type: int

    Get or set the velocity pixel count.

.. py:property:: range_window_type
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.range_window_type
    :type: ImageWindowType

    Get or set the range window type.

.. py:property:: range_window_side_lobe_level
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.range_window_side_lobe_level
    :type: float

    Get or set the range window side lobe level.

.. py:property:: velocity_window_type
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.velocity_window_type
    :type: ImageWindowType

    Get or set the velocity window type.

.. py:property:: velocity_window_side_lobe_level
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.velocity_window_side_lobe_level
    :type: float

    Get or set the velocity window side lobe level.

.. py:property:: range_resolution
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.range_resolution
    :type: float

    Get or set the range resolution.

.. py:property:: range_window_size
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.range_window_size
    :type: float

    Get or set the range window size.

.. py:property:: cross_range_resolution
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.cross_range_resolution
    :type: float

    Get or set the cross range resolution.

.. py:property:: cross_range_window_size
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.cross_range_window_size
    :type: float

    Get or set the cross range window size.

.. py:property:: required_bandwidth
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.required_bandwidth
    :type: float

    Get the waveform product's required bandwidth.

.. py:property:: collection_angle
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.collection_angle
    :type: float

    Get the waveform collection angle.

.. py:property:: frequency_samples_per_pulse
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.frequency_samples_per_pulse
    :type: int

    Get the number of frequency samples per pulse.

.. py:property:: minimum_pulse_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.minimum_pulse_count
    :type: int

    Get the minimum pulse count.

.. py:property:: identifier
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct.identifier
    :type: str

    Get the unique identifier for the data product


