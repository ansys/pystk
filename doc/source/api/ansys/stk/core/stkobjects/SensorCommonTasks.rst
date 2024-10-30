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



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorCommonTasks



Method detail
-------------

.. py:method:: set_pattern_simple_conic(self, coneAngle: typing.Any, angularResolution: typing.Any) -> SensorSimpleConicPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_simple_conic

    Define the sensor using a simple conic pattern.

    :Parameters:

    **coneAngle** : :obj:`~typing.Any`
    **angularResolution** : :obj:`~typing.Any`

    :Returns:

        :obj:`~SensorSimpleConicPattern`

.. py:method:: set_pattern_complex_conic(self, innerConeHalfAngle: typing.Any, outerConeHalfAngle: typing.Any, minimumClockAngle: typing.Any, maximumClockAngle: typing.Any) -> SensorComplexConicPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_complex_conic

    Define the sensor using a complex conic pattern.

    :Parameters:

    **innerConeHalfAngle** : :obj:`~typing.Any`
    **outerConeHalfAngle** : :obj:`~typing.Any`
    **minimumClockAngle** : :obj:`~typing.Any`
    **maximumClockAngle** : :obj:`~typing.Any`

    :Returns:

        :obj:`~SensorComplexConicPattern`

.. py:method:: set_pattern_eoir(self, lineOfSiteJitter: float, eProcessingLevel: SENSOR_EOIR_PROCESSING_LEVEL_TYPE) -> SensorEOIRPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_eoir

    Define the sensor using a EOIR pattern.

    :Parameters:

    **lineOfSiteJitter** : :obj:`~float`
    **eProcessingLevel** : :obj:`~SENSOR_EOIR_PROCESSING_LEVEL_TYPE`

    :Returns:

        :obj:`~SensorEOIRPattern`

.. py:method:: set_pattern_half_power(self, frequency: float, antennaDiameter: float, angularResolution: typing.Any) -> SensorHalfPowerPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_half_power

    Define the sensor using a half power pattern.

    :Parameters:

    **frequency** : :obj:`~float`
    **antennaDiameter** : :obj:`~float`
    **angularResolution** : :obj:`~typing.Any`

    :Returns:

        :obj:`~SensorHalfPowerPattern`

.. py:method:: set_pattern_rectangular(self, verticalHalfAngle: typing.Any, horizontalHalfAngle: typing.Any) -> SensorRectangularPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_rectangular

    Define the sensor using a rectangular pattern.

    :Parameters:

    **verticalHalfAngle** : :obj:`~typing.Any`
    **horizontalHalfAngle** : :obj:`~typing.Any`

    :Returns:

        :obj:`~SensorRectangularPattern`

.. py:method:: set_pattern_custom(self, filename: str) -> SensorCustomPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_custom

    Define the sensor using a custom pattern.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~SensorCustomPattern`

.. py:method:: set_pattern_sar(self, minElevationAngle: typing.Any, maxElevationAngle: typing.Any, foreExclusionAngle: typing.Any, aftExclusionAngle: typing.Any, parentAltitude: float) -> SensorSARPattern
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pattern_sar

    Define the sensor using a SAR pattern.

    :Parameters:

    **minElevationAngle** : :obj:`~typing.Any`
    **maxElevationAngle** : :obj:`~typing.Any`
    **foreExclusionAngle** : :obj:`~typing.Any`
    **aftExclusionAngle** : :obj:`~typing.Any`
    **parentAltitude** : :obj:`~float`

    :Returns:

        :obj:`~SensorSARPattern`

.. py:method:: set_pointing_fixed_az_el(self, azimuth: typing.Any, elevation: typing.Any, aboutBoresight: AZ_EL_ABOUT_BORESIGHT) -> SensorPointingFixed
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_az_el

    Set the pointing method to Fixed with an AzEl orientation.

    :Parameters:

    **azimuth** : :obj:`~typing.Any`
    **elevation** : :obj:`~typing.Any`
    **aboutBoresight** : :obj:`~AZ_EL_ABOUT_BORESIGHT`

    :Returns:

        :obj:`~SensorPointingFixed`

.. py:method:: set_pointing_fixed_euler(self, sequence: EULER_ORIENTATION_SEQUENCE_TYPE, a: typing.Any, b: typing.Any, c: typing.Any) -> SensorPointingFixed
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_euler

    Set the pointing method to Fixed with a Euler Angles orientation.

    :Parameters:

    **sequence** : :obj:`~EULER_ORIENTATION_SEQUENCE_TYPE`
    **a** : :obj:`~typing.Any`
    **b** : :obj:`~typing.Any`
    **c** : :obj:`~typing.Any`

    :Returns:

        :obj:`~SensorPointingFixed`

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

.. py:method:: set_pointing_fixed_ypr(self, sequence: YPR_ANGLES_SEQUENCE, yaw: typing.Any, pitch: typing.Any, roll: typing.Any) -> SensorPointingFixed
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_ypr

    Set the pointing method to Fixed with a YPR Angles orientation.

    :Parameters:

    **sequence** : :obj:`~YPR_ANGLES_SEQUENCE`
    **yaw** : :obj:`~typing.Any`
    **pitch** : :obj:`~typing.Any`
    **roll** : :obj:`~typing.Any`

    :Returns:

        :obj:`~SensorPointingFixed`

.. py:method:: set_pointing_fixed_axes_az_el(self, referenceAxes: str, azimuth: typing.Any, elevation: typing.Any, aboutBoresight: AZ_EL_ABOUT_BORESIGHT) -> SensorPointingFixedInAxes
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_az_el

    Set the pointing method to FixedAxes with an AzEl orientation.

    :Parameters:

    **referenceAxes** : :obj:`~str`
    **azimuth** : :obj:`~typing.Any`
    **elevation** : :obj:`~typing.Any`
    **aboutBoresight** : :obj:`~AZ_EL_ABOUT_BORESIGHT`

    :Returns:

        :obj:`~SensorPointingFixedInAxes`

.. py:method:: set_pointing_fixed_axes_euler(self, referenceAxes: str, sequence: EULER_ORIENTATION_SEQUENCE_TYPE, a: typing.Any, b: typing.Any, c: typing.Any) -> SensorPointingFixedInAxes
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_euler

    Set the pointing method to FixedAxes with a Euler Angles orientation.

    :Parameters:

    **referenceAxes** : :obj:`~str`
    **sequence** : :obj:`~EULER_ORIENTATION_SEQUENCE_TYPE`
    **a** : :obj:`~typing.Any`
    **b** : :obj:`~typing.Any`
    **c** : :obj:`~typing.Any`

    :Returns:

        :obj:`~SensorPointingFixedInAxes`

.. py:method:: set_pointing_fixed_axes_quaternion(self, referenceAxes: str, qx: float, qy: float, qz: float, qs: float) -> SensorPointingFixedInAxes
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_quaternion

    Set the pointing method to FixedAxes with a Quaternion orientation.

    :Parameters:

    **referenceAxes** : :obj:`~str`
    **qx** : :obj:`~float`
    **qy** : :obj:`~float`
    **qz** : :obj:`~float`
    **qs** : :obj:`~float`

    :Returns:

        :obj:`~SensorPointingFixedInAxes`

.. py:method:: set_pointing_fixed_axes_ypr(self, referenceAxes: str, sequence: YPR_ANGLES_SEQUENCE, yaw: typing.Any, pitch: typing.Any, roll: typing.Any) -> SensorPointingFixedInAxes
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_fixed_axes_ypr

    Set the pointing method to FixedAxes with a YPR Angles orientation.

    :Parameters:

    **referenceAxes** : :obj:`~str`
    **sequence** : :obj:`~YPR_ANGLES_SEQUENCE`
    **yaw** : :obj:`~typing.Any`
    **pitch** : :obj:`~typing.Any`
    **roll** : :obj:`~typing.Any`

    :Returns:

        :obj:`~SensorPointingFixedInAxes`

.. py:method:: set_pointing_3d_model(self, attachName: str) -> SensorPointing3DModel
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_3d_model

    Set the pointing method to 3DModel.

    :Parameters:

    **attachName** : :obj:`~str`

    :Returns:

        :obj:`~SensorPointing3DModel`

.. py:method:: set_pointing_grazing_altitude(self, azimuthOffset: typing.Any, grazingAlt: float) -> SensorPointingGrazingAltitude
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_grazing_altitude

    Set the pointing method to GrazingAlt.

    :Parameters:

    **azimuthOffset** : :obj:`~typing.Any`
    **grazingAlt** : :obj:`~float`

    :Returns:

        :obj:`~SensorPointingGrazingAltitude`

.. py:method:: set_pointing_spinning(self, spinAxisAzimuth: typing.Any, spinAxisElevation: typing.Any, spinAxisConeAngle: typing.Any, scanMode: SENSOR_SCAN_MODE, spinRate: float, offsetAngle: typing.Any, clockAngleStart: typing.Any, clockAngleStop: typing.Any) -> SensorPointingSpinning
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_spinning

    Set the pointing method to Spinning.

    :Parameters:

    **spinAxisAzimuth** : :obj:`~typing.Any`
    **spinAxisElevation** : :obj:`~typing.Any`
    **spinAxisConeAngle** : :obj:`~typing.Any`
    **scanMode** : :obj:`~SENSOR_SCAN_MODE`
    **spinRate** : :obj:`~float`
    **offsetAngle** : :obj:`~typing.Any`
    **clockAngleStart** : :obj:`~typing.Any`
    **clockAngleStop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~SensorPointingSpinning`

.. py:method:: set_pointing_targeted_tracking(self, trackModeType: TRACK_MODE, aboutBoresightType: BORESIGHT_TYPE, targetPath: str) -> SensorPointingTargeted
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_targeted_tracking

    Set the pointing method to Targeted with Tracking.

    :Parameters:

    **trackModeType** : :obj:`~TRACK_MODE`
    **aboutBoresightType** : :obj:`~BORESIGHT_TYPE`
    **targetPath** : :obj:`~str`

    :Returns:

        :obj:`~SensorPointingTargeted`

.. py:method:: set_pointing_along_vector(self, alignmentVector: str, constraintVector: str, clockAngleOffset: typing.Any) -> SensorPointingAlongVector
    :canonical: ansys.stk.core.stkobjects.SensorCommonTasks.set_pointing_along_vector

    Set the pointing method to Along Vector.

    :Parameters:

    **alignmentVector** : :obj:`~str`
    **constraintVector** : :obj:`~str`
    **clockAngleOffset** : :obj:`~typing.Any`

    :Returns:

        :obj:`~SensorPointingAlongVector`

