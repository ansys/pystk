SensorCommonTasks
=================

.. py:class:: ansys.stk.core.stkobjects.SensorCommonTasks

   Class defining the Sensor Common class.

.. py:currentmodule:: SensorCommonTasks

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_simple_conic`
              - Define the sensor using a simple conic pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_complex_conic`
              - Define the sensor using a complex conic pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_eoir`
              - Define the sensor using a EOIR pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_half_power`
              - Define the sensor using a half power pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_rectangular`
              - Define the sensor using a rectangular pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_custom`
              - Define the sensor using a custom pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_sar`
              - Define the sensor using a SAR pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_az_el`
              - Set the pointing method to Fixed with an AzEl orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_euler`
              - Set the pointing method to Fixed with a Euler Angles orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_quaternion`
              - Set the pointing method to Fixed with a Quaternion orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_ypr`
              - Set the pointing method to Fixed with a YPR Angles orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_az_el`
              - Set the pointing method to FixedAxes with an AzEl orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_euler`
              - Set the pointing method to FixedAxes with a Euler Angles orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_quaternion`
              - Set the pointing method to FixedAxes with a Quaternion orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_ypr`
              - Set the pointing method to FixedAxes with a YPR Angles orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_3d_model`
              - Set the pointing method to 3DModel.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_grazing_altitude`
              - Set the pointing method to GrazingAlt.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_spinning`
              - Set the pointing method to Spinning.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_targeted_tracking`
              - Set the pointing method to Targeted with Tracking.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_along_vector`
              - Set the pointing method to Along Vector.


Examples
--------

Define sensor pointing fixed axes YPR

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_ypr(
        "CentralBody/Sun J2000 Axes", YPRAnglesSequence.RYP, 11, 22, 33
    )


Define sensor pointing fixed YPR

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_ypr(YPRAnglesSequence.RPY, 12, 24, 36)


Define sensor pointing fixed axes Quaternion

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_quaternion(
        "CentralBody/Sun J2000 Axes", 0.1, 0.2, 0.3, 0.4
    )


Define sensor pointing fixed Quaternion

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_quaternion(0.1, 0.2, 0.3, 0.4)


Define sensor pointing fixed axes Euler

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_euler(
        "CentralBody/Sun J2000 Axes", EulerOrientationSequenceType.SEQUENCE_132, 30, 40, 50
    )


Define sensor pointing fixed Euler

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_euler(
        EulerOrientationSequenceType.SEQUENCE_132, 30, 40, 50
    )


Define sensor pointing fixed axes AzEl

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_az_el(
        "CentralBody/Sun J2000 Axes", 11, 22, AzElAboutBoresight.HOLD
    )


Define sensor pointing fixed AzEl

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_az_el(4.5, -45.0, AzElAboutBoresight.ROTATE)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorCommonTasks



Method detail
-------------

.. py:method:: set_pattern_simple_conic(self, cone_angle: typing.Any, angular_resolution: typing.Any) -> SensorSimpleConicPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_simple_conic

    Define the sensor using a simple conic pattern.

    :Parameters:

        **cone_angle** : :obj:`~typing.Any`

        **angular_resolution** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SensorSimpleConicPattern`

.. py:method:: set_pattern_complex_conic(self, inner_cone_half_angle: typing.Any, outer_cone_half_angle: typing.Any, minimum_clock_angle: typing.Any, maximum_clock_angle: typing.Any) -> SensorComplexConicPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_complex_conic

    Define the sensor using a complex conic pattern.

    :Parameters:

        **inner_cone_half_angle** : :obj:`~typing.Any`

        **outer_cone_half_angle** : :obj:`~typing.Any`

        **minimum_clock_angle** : :obj:`~typing.Any`

        **maximum_clock_angle** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SensorComplexConicPattern`

.. py:method:: set_pattern_eoir(self, line_of_site_jitter: float, processing_level: SensorEOIRProcessingLevelType) -> SensorEOIRPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_eoir

    Define the sensor using a EOIR pattern.

    :Parameters:

        **line_of_site_jitter** : :obj:`~float`

        **processing_level** : :obj:`~SensorEOIRProcessingLevelType`


    :Returns:

        :obj:`~SensorEOIRPattern`

.. py:method:: set_pattern_half_power(self, frequency: float, antenna_diameter: float, angular_resolution: typing.Any) -> SensorHalfPowerPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_half_power

    Define the sensor using a half power pattern.

    :Parameters:

        **frequency** : :obj:`~float`

        **antenna_diameter** : :obj:`~float`

        **angular_resolution** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SensorHalfPowerPattern`

.. py:method:: set_pattern_rectangular(self, vertical_half_angle: typing.Any, horizontal_half_angle: typing.Any) -> SensorRectangularPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_rectangular

    Define the sensor using a rectangular pattern.

    :Parameters:

        **vertical_half_angle** : :obj:`~typing.Any`

        **horizontal_half_angle** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SensorRectangularPattern`

.. py:method:: set_pattern_custom(self, filename: str) -> SensorCustomPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_custom

    Define the sensor using a custom pattern.

    :Parameters:

        **filename** : :obj:`~str`


    :Returns:

        :obj:`~SensorCustomPattern`

.. py:method:: set_pattern_sar(self, min_elevation_angle: typing.Any, max_elevation_angle: typing.Any, fore_exclusion_angle: typing.Any, aft_exclusion_angle: typing.Any, parent_altitude: float) -> SensorSARPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_sar

    Define the sensor using a SAR pattern.

    :Parameters:

        **min_elevation_angle** : :obj:`~typing.Any`

        **max_elevation_angle** : :obj:`~typing.Any`

        **fore_exclusion_angle** : :obj:`~typing.Any`

        **aft_exclusion_angle** : :obj:`~typing.Any`

        **parent_altitude** : :obj:`~float`


    :Returns:

        :obj:`~SensorSARPattern`

.. py:method:: set_pointing_fixed_az_el(self, azimuth: typing.Any, elevation: typing.Any, about_boresight: AzElAboutBoresight) -> SensorPointingFixed
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_az_el

    Set the pointing method to Fixed with an AzEl orientation.

    :Parameters:

        **azimuth** : :obj:`~typing.Any`

        **elevation** : :obj:`~typing.Any`

        **about_boresight** : :obj:`~AzElAboutBoresight`


    :Returns:

        :obj:`~SensorPointingFixed`

    Examples
    --------

    Define sensor pointing fixed AzEl

    .. code-block:: python

        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_az_el(4.5, -45.0, AzElAboutBoresight.ROTATE)


.. py:method:: set_pointing_fixed_euler(self, sequence: EulerOrientationSequenceType, a: typing.Any, b: typing.Any, c: typing.Any) -> SensorPointingFixed
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_euler

    Set the pointing method to Fixed with a Euler Angles orientation.

    :Parameters:

        **sequence** : :obj:`~EulerOrientationSequenceType`

        **a** : :obj:`~typing.Any`

        **b** : :obj:`~typing.Any`

        **c** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SensorPointingFixed`

    Examples
    --------

    Define sensor pointing fixed Euler

    .. code-block:: python

        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_euler(
            EulerOrientationSequenceType.SEQUENCE_132, 30, 40, 50
        )


.. py:method:: set_pointing_fixed_quaternion(self, qx: float, qy: float, qz: float, qs: float) -> SensorPointingFixed
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_quaternion

    Set the pointing method to Fixed with a Quaternion orientation.

    :Parameters:

        **qx** : :obj:`~float`

        **qy** : :obj:`~float`

        **qz** : :obj:`~float`

        **qs** : :obj:`~float`


    :Returns:

        :obj:`~SensorPointingFixed`

    Examples
    --------

    Define sensor pointing fixed Quaternion

    .. code-block:: python

        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_quaternion(0.1, 0.2, 0.3, 0.4)


.. py:method:: set_pointing_fixed_ypr(self, sequence: YPRAnglesSequence, yaw: typing.Any, pitch: typing.Any, roll: typing.Any) -> SensorPointingFixed
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_ypr

    Set the pointing method to Fixed with a YPR Angles orientation.

    :Parameters:

        **sequence** : :obj:`~YPRAnglesSequence`

        **yaw** : :obj:`~typing.Any`

        **pitch** : :obj:`~typing.Any`

        **roll** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SensorPointingFixed`

    Examples
    --------

    Define sensor pointing fixed YPR

    .. code-block:: python

        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_ypr(YPRAnglesSequence.RPY, 12, 24, 36)


.. py:method:: set_pointing_fixed_axes_az_el(self, reference_axes: str, azimuth: typing.Any, elevation: typing.Any, about_boresight: AzElAboutBoresight) -> SensorPointingFixedInAxes
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_az_el

    Set the pointing method to FixedAxes with an AzEl orientation.

    :Parameters:

        **reference_axes** : :obj:`~str`

        **azimuth** : :obj:`~typing.Any`

        **elevation** : :obj:`~typing.Any`

        **about_boresight** : :obj:`~AzElAboutBoresight`


    :Returns:

        :obj:`~SensorPointingFixedInAxes`

    Examples
    --------

    Define sensor pointing fixed axes AzEl

    .. code-block:: python

        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_axes_az_el(
            "CentralBody/Sun J2000 Axes", 11, 22, AzElAboutBoresight.HOLD
        )


.. py:method:: set_pointing_fixed_axes_euler(self, reference_axes: str, sequence: EulerOrientationSequenceType, a: typing.Any, b: typing.Any, c: typing.Any) -> SensorPointingFixedInAxes
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_euler

    Set the pointing method to FixedAxes with a Euler Angles orientation.

    :Parameters:

        **reference_axes** : :obj:`~str`

        **sequence** : :obj:`~EulerOrientationSequenceType`

        **a** : :obj:`~typing.Any`

        **b** : :obj:`~typing.Any`

        **c** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SensorPointingFixedInAxes`

    Examples
    --------

    Define sensor pointing fixed axes Euler

    .. code-block:: python

        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_axes_euler(
            "CentralBody/Sun J2000 Axes", EulerOrientationSequenceType.SEQUENCE_132, 30, 40, 50
        )


.. py:method:: set_pointing_fixed_axes_quaternion(self, reference_axes: str, qx: float, qy: float, qz: float, qs: float) -> SensorPointingFixedInAxes
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_quaternion

    Set the pointing method to FixedAxes with a Quaternion orientation.

    :Parameters:

        **reference_axes** : :obj:`~str`

        **qx** : :obj:`~float`

        **qy** : :obj:`~float`

        **qz** : :obj:`~float`

        **qs** : :obj:`~float`


    :Returns:

        :obj:`~SensorPointingFixedInAxes`

    Examples
    --------

    Define sensor pointing fixed axes Quaternion

    .. code-block:: python

        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_axes_quaternion(
            "CentralBody/Sun J2000 Axes", 0.1, 0.2, 0.3, 0.4
        )


.. py:method:: set_pointing_fixed_axes_ypr(self, reference_axes: str, sequence: YPRAnglesSequence, yaw: typing.Any, pitch: typing.Any, roll: typing.Any) -> SensorPointingFixedInAxes
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_ypr

    Set the pointing method to FixedAxes with a YPR Angles orientation.

    :Parameters:

        **reference_axes** : :obj:`~str`

        **sequence** : :obj:`~YPRAnglesSequence`

        **yaw** : :obj:`~typing.Any`

        **pitch** : :obj:`~typing.Any`

        **roll** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SensorPointingFixedInAxes`

    Examples
    --------

    Define sensor pointing fixed axes YPR

    .. code-block:: python

        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_axes_ypr(
            "CentralBody/Sun J2000 Axes", YPRAnglesSequence.RYP, 11, 22, 33
        )


.. py:method:: set_pointing_3d_model(self, attach_name: str) -> SensorPointing3DModel
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_3d_model

    Set the pointing method to 3DModel.

    :Parameters:

        **attach_name** : :obj:`~str`


    :Returns:

        :obj:`~SensorPointing3DModel`

.. py:method:: set_pointing_grazing_altitude(self, azimuth_offset: typing.Any, grazing_alt: float) -> SensorPointingGrazingAltitude
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_grazing_altitude

    Set the pointing method to GrazingAlt.

    :Parameters:

        **azimuth_offset** : :obj:`~typing.Any`

        **grazing_alt** : :obj:`~float`


    :Returns:

        :obj:`~SensorPointingGrazingAltitude`

.. py:method:: set_pointing_spinning(self, spin_axis_azimuth: typing.Any, spin_axis_elevation: typing.Any, spin_axis_cone_angle: typing.Any, scan_mode: SensorScanMode, spin_rate: float, offset_angle: typing.Any, clock_angle_start: typing.Any, clock_angle_stop: typing.Any) -> SensorPointingSpinning
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_spinning

    Set the pointing method to Spinning.

    :Parameters:

        **spin_axis_azimuth** : :obj:`~typing.Any`

        **spin_axis_elevation** : :obj:`~typing.Any`

        **spin_axis_cone_angle** : :obj:`~typing.Any`

        **scan_mode** : :obj:`~SensorScanMode`

        **spin_rate** : :obj:`~float`

        **offset_angle** : :obj:`~typing.Any`

        **clock_angle_start** : :obj:`~typing.Any`

        **clock_angle_stop** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SensorPointingSpinning`

.. py:method:: set_pointing_targeted_tracking(self, track_mode_type: TrackMode, about_boresight_type: BoresightType, target_path: str) -> SensorPointingTargeted
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_targeted_tracking

    Set the pointing method to Targeted with Tracking.

    :Parameters:

        **track_mode_type** : :obj:`~TrackMode`

        **about_boresight_type** : :obj:`~BoresightType`

        **target_path** : :obj:`~str`


    :Returns:

        :obj:`~SensorPointingTargeted`

.. py:method:: set_pointing_along_vector(self, alignment_vector: str, constraint_vector: str, clock_angle_offset: typing.Any) -> SensorPointingAlongVector
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_along_vector

    Set the pointing method to Along Vector.

    :Parameters:

        **alignment_vector** : :obj:`~str`

        **constraint_vector** : :obj:`~str`

        **clock_angle_offset** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SensorPointingAlongVector`

