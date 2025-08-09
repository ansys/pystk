SensorGraphics3DPulse
=====================

.. py:class:: ansys.stk.core.stkobjects.SensorGraphics3DPulse

   Class defining 3D pulse properties of a Sensor.

.. py:currentmodule:: SensorGraphics3DPulse

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DPulse.reset_to_defaults`
              - Restore all default values for modulating a sensor's projection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DPulse.amplitude`
              - Amplitude, the transparent/opaque ratio of the pulses. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DPulse.enable_smooth`
              - Opt whether to enable averaging of pixels over the range of the pulse to achieve smoother, better viewing quality.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DPulse.frequency_value`
              - If ePulseFrequencyCustom is selected for the PreselFreq property, specify the custom frequency value. Uses Frequency Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DPulse.length`
              - Pulse length, how much physical space a given pulse occupies. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DPulse.pulse_frequency_preset`
              - Select a frequency option from the SensorGraphics3DPulseFrequencyPreset enumeration. Here, frequency refers to the rate at which pulses occur.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DPulse.show_pulses`
              - Enable display of pulses in the sensor's projection. If not enabled, the sensor projection is displayed as a transparent, homogeneous color.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DPulse.show_sensor_pulse_in_opposite_direction`
              - Opt whether to have the sensor pulse in a direction opposite from that which is set. This is useful if you want pulsing to display in the same direction as usual but pulsing is faster than the animation step.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DPulse.style`
              - Select an available sine or box style from the SensorGraphics3DPulseStyle enumeration. Box styles display a very sharp transition from enabled to disabled for the sensor's modulation, while the Sine styles display a smooth transition.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorGraphics3DPulse


Property detail
---------------

.. py:property:: amplitude
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DPulse.amplitude
    :type: float

    Amplitude, the transparent/opaque ratio of the pulses. Dimensionless.

.. py:property:: enable_smooth
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DPulse.enable_smooth
    :type: bool

    Opt whether to enable averaging of pixels over the range of the pulse to achieve smoother, better viewing quality.

.. py:property:: frequency_value
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DPulse.frequency_value
    :type: float

    If ePulseFrequencyCustom is selected for the PreselFreq property, specify the custom frequency value. Uses Frequency Dimension.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DPulse.length
    :type: float

    Pulse length, how much physical space a given pulse occupies. Uses Distance Dimension.

.. py:property:: pulse_frequency_preset
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DPulse.pulse_frequency_preset
    :type: SensorGraphics3DPulseFrequencyPreset

    Select a frequency option from the SensorGraphics3DPulseFrequencyPreset enumeration. Here, frequency refers to the rate at which pulses occur.

.. py:property:: show_pulses
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DPulse.show_pulses
    :type: bool

    Enable display of pulses in the sensor's projection. If not enabled, the sensor projection is displayed as a transparent, homogeneous color.

.. py:property:: show_sensor_pulse_in_opposite_direction
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DPulse.show_sensor_pulse_in_opposite_direction
    :type: bool

    Opt whether to have the sensor pulse in a direction opposite from that which is set. This is useful if you want pulsing to display in the same direction as usual but pulsing is faster than the animation step.

.. py:property:: style
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DPulse.style
    :type: SensorGraphics3DPulseStyle

    Select an available sine or box style from the SensorGraphics3DPulseStyle enumeration. Box styles display a very sharp transition from enabled to disabled for the sensor's modulation, while the Sine styles display a smooth transition.


Method detail
-------------















.. py:method:: reset_to_defaults(self) -> None
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DPulse.reset_to_defaults

    Restore all default values for modulating a sensor's projection.

    :Returns:

        :obj:`~None`



