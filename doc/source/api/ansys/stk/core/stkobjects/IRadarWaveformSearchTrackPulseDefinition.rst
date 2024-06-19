IRadarWaveformSearchTrackPulseDefinition
========================================

.. py:class:: IRadarWaveformSearchTrackPulseDefinition

   object
   
   Provide access to the properties and methods defining the pulse definition for a search track waveform.

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
            * - :py:meth:`~unambiguous_velocity`
            * - :py:meth:`~pulse_width_mode`
            * - :py:meth:`~pulse_width`
            * - :py:meth:`~duty_factor`
            * - :py:meth:`~number_of_pulses`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarWaveformSearchTrackPulseDefinition


Property detail
---------------

.. py:property:: prf_mode
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSearchTrackPulseDefinition.prf_mode
    :type: RADAR_SEARCH_TRACK_PRF_MODE

    Gets or sets the prf mode enumeration.

.. py:property:: prf
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSearchTrackPulseDefinition.prf
    :type: float

    Gets or sets the pulse repetition frequency.

.. py:property:: unambiguous_range
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSearchTrackPulseDefinition.unambiguous_range
    :type: float

    Gets or sets the unambiguous range.

.. py:property:: unambiguous_velocity
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSearchTrackPulseDefinition.unambiguous_velocity
    :type: float

    Gets or sets the unambiguous velocity.

.. py:property:: pulse_width_mode
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSearchTrackPulseDefinition.pulse_width_mode
    :type: RADAR_SEARCH_TRACK_PULSE_WIDTH_MODE

    Gets or sets the pulse width mode enumeration.

.. py:property:: pulse_width
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSearchTrackPulseDefinition.pulse_width
    :type: float

    Gets or sets the pulse width.

.. py:property:: duty_factor
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSearchTrackPulseDefinition.duty_factor
    :type: float

    Gets or sets the duty factor.

.. py:property:: number_of_pulses
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSearchTrackPulseDefinition.number_of_pulses
    :type: int

    Gets or sets the number of pulses.


