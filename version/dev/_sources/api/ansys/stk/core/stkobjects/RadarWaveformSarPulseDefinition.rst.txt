RadarWaveformSarPulseDefinition
===============================

.. py:class:: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition

   Class defining the pulse definition for a SAR waveform.

.. py:currentmodule:: RadarWaveformSarPulseDefinition

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.bandwidth`
              - Get or set the bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.fm_chirp_rate`
              - Get or set the FM chirp rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.if_bandwidth`
              - Get or set the IF bandwidth. This property is read only for monostatic radar systems.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.number_of_pulses`
              - Get or set the number of pulses.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_compression_ratio`
              - Get or set the pulse compression ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_compression_ratio_mode`
              - Get or set the pulse compression ratio mode enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_repetition_frequency`
              - Get or set the pulse repetition frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_repetition_frequency_mode`
              - Get or set the prf mode enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_width`
              - Get or set the pulse width.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_broadening_factor`
              - Get or set the range broadening factor. This property is read only for monostatic radar systems.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_resolution`
              - Get or set the range resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_resolution_mode`
              - Get or set the range resolution mode enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.scene_depth`
              - Get or set the scene depth.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.unambiguous_range`
              - Get or set the unambiguous range.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarWaveformSarPulseDefinition


Property detail
---------------

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.bandwidth
    :type: float

    Get or set the bandwidth.

.. py:property:: fm_chirp_rate
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.fm_chirp_rate
    :type: float

    Get or set the FM chirp rate.

.. py:property:: if_bandwidth
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.if_bandwidth
    :type: float

    Get or set the IF bandwidth. This property is read only for monostatic radar systems.

.. py:property:: number_of_pulses
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.number_of_pulses
    :type: int

    Get or set the number of pulses.

.. py:property:: pulse_compression_ratio
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_compression_ratio
    :type: float

    Get or set the pulse compression ratio.

.. py:property:: pulse_compression_ratio_mode
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_compression_ratio_mode
    :type: RadarSarPcrMode

    Get or set the pulse compression ratio mode enumeration.

.. py:property:: pulse_repetition_frequency
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_repetition_frequency
    :type: float

    Get or set the pulse repetition frequency.

.. py:property:: pulse_repetition_frequency_mode
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_repetition_frequency_mode
    :type: RadarSarPRFMode

    Get or set the prf mode enumeration.

.. py:property:: pulse_width
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_width
    :type: float

    Get or set the pulse width.

.. py:property:: range_broadening_factor
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_broadening_factor
    :type: float

    Get or set the range broadening factor. This property is read only for monostatic radar systems.

.. py:property:: range_resolution
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_resolution
    :type: float

    Get or set the range resolution.

.. py:property:: range_resolution_mode
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_resolution_mode
    :type: RadarSarRangeResolutionMode

    Get or set the range resolution mode enumeration.

.. py:property:: scene_depth
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.scene_depth
    :type: float

    Get or set the scene depth.

.. py:property:: unambiguous_range
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.unambiguous_range
    :type: float

    Get or set the unambiguous range.


