RadarWaveformBistaticReceiverSearchTrackContinuous
==================================================

.. py:class:: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackContinuous

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarWaveformSearchTrack`

   Class defining a bistatic receiver continuous waveform.

.. py:currentmodule:: RadarWaveformBistaticReceiverSearchTrackContinuous

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackContinuous.analysis_mode_type`
              - Gets or sets the analysis type.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackContinuous.analysis_mode`
              - Gets the interface for setting analysis parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackContinuous.probability_of_false_alarm`
              - Gets or sets the probability of false alarm.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarWaveformBistaticReceiverSearchTrackContinuous


Property detail
---------------

.. py:property:: analysis_mode_type
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackContinuous.analysis_mode_type
    :type: RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE

    Gets or sets the analysis type.

.. py:property:: analysis_mode
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackContinuous.analysis_mode
    :type: IRadarContinuousWaveAnalysisMode

    Gets the interface for setting analysis parameters.

.. py:property:: probability_of_false_alarm
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackContinuous.probability_of_false_alarm
    :type: float

    Gets or sets the probability of false alarm.


