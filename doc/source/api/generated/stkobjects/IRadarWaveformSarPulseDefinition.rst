IRadarWaveformSarPulseDefinition
================================

.. py:class:: IRadarWaveformSarPulseDefinition

   object
   
   Provide access to the properties and methods defining the pulse definition for a Sar waveform.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~prf_mode`
            * - :py:meth:`~prf`
            * - :py:meth:`~unambiguous_range`
            * - :py:meth:`~range_resolution_mode`
            * - :py:meth:`~range_resolution`
            * - :py:meth:`~bandwidth`
            * - :py:meth:`~pcr_mode`
            * - :py:meth:`~pcr`
            * - :py:meth:`~pulse_width`
            * - :py:meth:`~scene_depth`
            * - :py:meth:`~fm_chirp_rate`
            * - :py:meth:`~range_broadening_factor`
            * - :py:meth:`~if_bandwidth`
            * - :py:meth:`~number_of_pulses`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarWaveformSarPulseDefinition


Property detail
---------------

.. py:property:: prf_mode
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.prf_mode
    :type: "RADAR_SAR_PRF_MODE"

    Gets or sets the prf mode enumeration.

.. py:property:: prf
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.prf
    :type: float

    Gets or sets the pulse repetition frequency.

.. py:property:: unambiguous_range
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.unambiguous_range
    :type: float

    Gets or sets the unambiguous range.

.. py:property:: range_resolution_mode
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.range_resolution_mode
    :type: "RADAR_SAR_RANGE_RESOLUTION_MODE"

    Gets or sets the range resolution mode enumeration.

.. py:property:: range_resolution
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.range_resolution
    :type: float

    Gets or sets the range resolution.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.bandwidth
    :type: float

    Gets or sets the bandwidth.

.. py:property:: pcr_mode
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.pcr_mode
    :type: "RADAR_SAR_PCR_MODE"

    Gets or sets the pulse compression ratio mode enumeration.

.. py:property:: pcr
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.pcr
    :type: float

    Gets or sets the pulse compression ratio.

.. py:property:: pulse_width
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.pulse_width
    :type: float

    Gets or sets the pulse width.

.. py:property:: scene_depth
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.scene_depth
    :type: float

    Gets or sets the scene depth.

.. py:property:: fm_chirp_rate
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.fm_chirp_rate
    :type: float

    Gets or sets the FM chirp rate.

.. py:property:: range_broadening_factor
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.range_broadening_factor
    :type: float

    Gets or sets the range broadening factor. This property is read only for monostatic radar systems.

.. py:property:: if_bandwidth
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.if_bandwidth
    :type: float

    Gets or sets the IF bandwidth. This property is read only for monostatic radar systems.

.. py:property:: number_of_pulses
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseDefinition.number_of_pulses
    :type: int

    Gets or sets the number of pulses.


