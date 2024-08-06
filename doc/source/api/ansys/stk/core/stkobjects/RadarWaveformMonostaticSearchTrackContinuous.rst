RadarWaveformMonostaticSearchTrackContinuous
============================================

.. py:class:: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarWaveformSearchTrack`

   Class defining a monostatic continuous waveform.

.. py:currentmodule:: RadarWaveformMonostaticSearchTrackContinuous

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous.analysis_mode_type`
              - Gets or sets the analysis type.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous.analysis_mode`
              - Gets the interface for setting analysis parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous.probability_of_false_alarm`
              - Gets or sets the probability of false alarm.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous.modulator`
              - Gets the interface for setting the modulator parameters.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarWaveformMonostaticSearchTrackContinuous


Property detail
---------------

.. py:property:: analysis_mode_type
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous.analysis_mode_type
    :type: RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE

    Gets or sets the analysis type.

.. py:property:: analysis_mode
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous.analysis_mode
    :type: IRadarContinuousWaveAnalysisMode

    Gets the interface for setting analysis parameters.

.. py:property:: probability_of_false_alarm
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous.probability_of_false_alarm
    :type: float

    Gets or sets the probability of false alarm.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous.modulator
    :type: RadarModulator

    Gets the interface for setting the modulator parameters.


