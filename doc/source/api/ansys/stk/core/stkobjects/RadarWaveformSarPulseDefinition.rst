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

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_repetition_frequency_mode`
              - Gets or sets the prf mode enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_repetition_frequency`
              - Gets or sets the pulse repetition frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.unambiguous_range`
              - Gets or sets the unambiguous range.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_resolution_mode`
              - Gets or sets the range resolution mode enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_resolution`
              - Gets or sets the range resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.bandwidth`
              - Gets or sets the bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_compression_ratio_mode`
              - Gets or sets the pulse compression ratio mode enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_compression_ratio`
              - Gets or sets the pulse compression ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_width`
              - Gets or sets the pulse width.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.scene_depth`
              - Gets or sets the scene depth.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.fm_chirp_rate`
              - Gets or sets the FM chirp rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_broadening_factor`
              - Gets or sets the range broadening factor. This property is read only for monostatic radar systems.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.if_bandwidth`
              - Gets or sets the IF bandwidth. This property is read only for monostatic radar systems.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.number_of_pulses`
              - Gets or sets the number of pulses.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarWaveformSarPulseDefinition


Property detail
---------------

.. py:property:: pulse_repetition_frequency_mode
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_repetition_frequency_mode
    :type: RadarSarPRFMode

    Gets or sets the prf mode enumeration.

.. py:property:: pulse_repetition_frequency
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_repetition_frequency
    :type: float

    Gets or sets the pulse repetition frequency.

.. py:property:: unambiguous_range
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.unambiguous_range
    :type: float

    Gets or sets the unambiguous range.

.. py:property:: range_resolution_mode
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_resolution_mode
    :type: RadarSarRangeResolutionMode

    Gets or sets the range resolution mode enumeration.

.. py:property:: range_resolution
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_resolution
    :type: float

    Gets or sets the range resolution.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.bandwidth
    :type: float

    Gets or sets the bandwidth.

.. py:property:: pulse_compression_ratio_mode
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_compression_ratio_mode
    :type: RadarSarPcrMode

    Gets or sets the pulse compression ratio mode enumeration.

.. py:property:: pulse_compression_ratio
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_compression_ratio
    :type: float

    Gets or sets the pulse compression ratio.

.. py:property:: pulse_width
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.pulse_width
    :type: float

    Gets or sets the pulse width.

.. py:property:: scene_depth
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.scene_depth
    :type: float

    Gets or sets the scene depth.

.. py:property:: fm_chirp_rate
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.fm_chirp_rate
    :type: float

    Gets or sets the FM chirp rate.

.. py:property:: range_broadening_factor
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.range_broadening_factor
    :type: float

    Gets or sets the range broadening factor. This property is read only for monostatic radar systems.

.. py:property:: if_bandwidth
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.if_bandwidth
    :type: float

    Gets or sets the IF bandwidth. This property is read only for monostatic radar systems.

.. py:property:: number_of_pulses
    :canonical: ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition.number_of_pulses
    :type: int

    Gets or sets the number of pulses.


