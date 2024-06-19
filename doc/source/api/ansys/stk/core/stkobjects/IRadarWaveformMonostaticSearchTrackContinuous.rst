IRadarWaveformMonostaticSearchTrackContinuous
=============================================

.. py:class:: IRadarWaveformMonostaticSearchTrackContinuous

   object
   
   Interface which is implemented by a search/track waveform.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~analysis_mode_type`
            * - :py:meth:`~analysis_mode`
            * - :py:meth:`~probability_of_false_alarm`
            * - :py:meth:`~modulator`


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
    :type: IAgRadarContinuousWaveAnalysisMode

    Gets the interface for setting analysis parameters.

.. py:property:: probability_of_false_alarm
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackContinuous.probability_of_false_alarm
    :type: float

    Gets or sets the probability of false alarm.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackContinuous.modulator
    :type: IAgRadarModulator

    Gets the interface for setting the modulator parameters.


