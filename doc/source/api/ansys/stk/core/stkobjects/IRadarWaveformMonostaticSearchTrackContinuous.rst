IRadarWaveformMonostaticSearchTrackContinuous
=============================================

.. py:class:: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackContinuous

   object
   
   Interface which is implemented by a search/track waveform.

.. py:currentmodule:: IRadarWaveformMonostaticSearchTrackContinuous

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackContinuous.analysis_mode_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackContinuous.analysis_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackContinuous.probability_of_false_alarm`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackContinuous.modulator`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarWaveformMonostaticSearchTrackContinuous


Property detail
---------------

.. py:property:: analysis_mode_type
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackContinuous.analysis_mode_type
    :type: RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE

    Gets or sets the analysis type.

.. py:property:: analysis_mode
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackContinuous.analysis_mode
    :type: IRadarContinuousWaveAnalysisMode

    Gets the interface for setting analysis parameters.

.. py:property:: probability_of_false_alarm
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackContinuous.probability_of_false_alarm
    :type: float

    Gets or sets the probability of false alarm.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackContinuous.modulator
    :type: IRadarModulator

    Gets the interface for setting the modulator parameters.


