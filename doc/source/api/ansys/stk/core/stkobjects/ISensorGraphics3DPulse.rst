ISensorGraphics3DPulse
======================

.. py:class:: ISensorGraphics3DPulse

   object
   
   IAgSnVOPulse Interface, for setting and retrieving 3D Graphics Pulse properties of a sensor.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reset_to_defaults`
              - Restore all default values for modulating a sensor's projection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~pulse_visible`
            * - :py:meth:`~amplitude`
            * - :py:meth:`~length`
            * - :py:meth:`~style`
            * - :py:meth:`~enable_smooth`
            * - :py:meth:`~presel_freq`
            * - :py:meth:`~freq_value`
            * - :py:meth:`~freq_reverse_direction`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorGraphics3DPulse


Property detail
---------------

.. py:property:: pulse_visible
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3DPulse.pulse_visible
    :type: bool

    Enable display of pulses in the sensor's projection. If not enabled, the sensor projection is displayed as a transparent, homogeneous color.

.. py:property:: amplitude
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3DPulse.amplitude
    :type: float

    Amplitude, the transparent/opaque ratio of the pulses. Dimensionless.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3DPulse.length
    :type: float

    Pulse length, how much physical space a given pulse occupies. Uses Distance Dimension.

.. py:property:: style
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3DPulse.style
    :type: SENSOR_GRAPHICS_3D_PULSE_STYLE

    Select an available sine or box style from the AgESnVOPulseStyle enumeration. Box styles display a very sharp transition from enabled to disabled for the sensor's modulation, while the Sine styles display a smooth transition.

.. py:property:: enable_smooth
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3DPulse.enable_smooth
    :type: bool

    Opt whether to enable averaging of pixels over the range of the pulse to achieve smoother, better viewing quality.

.. py:property:: presel_freq
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3DPulse.presel_freq
    :type: SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET

    Select a frequency option from the AgESnVOPulseFrequencyPreset enumeration. Here, frequency refers to the rate at which pulses occur.

.. py:property:: freq_value
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3DPulse.freq_value
    :type: float

    If ePulseFrequencyCustom is selected for the PreselFreq property, specify the custom frequency value. Uses Frequency Dimension.

.. py:property:: freq_reverse_direction
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3DPulse.freq_reverse_direction
    :type: bool

    Opt whether to have the sensor pulse in a direction opposite from that which is set. This is useful if you want pulsing to display in the same direction as usual but pulsing is faster than the animation step.


Method detail
-------------

















.. py:method:: reset_to_defaults(self) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3DPulse.reset_to_defaults

    Restore all default values for modulating a sensor's projection.

    :Returns:

        :obj:`~None`

