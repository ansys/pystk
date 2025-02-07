RadarWaveformMonostaticSearchTrackFixedPRF
==========================================

.. py:class:: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarWaveformSearchTrack`

   Class defining a monostatic fixed PRF waveform.

.. py:currentmodule:: RadarWaveformMonostaticSearchTrackFixedPRF

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.set_probability_of_detection`
              - Set the probability of detection algorithm by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.pulse_definition`
              - Get the interface for setting the pulse definition parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.modulator`
              - Get the interface for setting the modulator parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.supported_probability_of_detection`
              - Get an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.probability_of_detection`
              - Get the interface for setting the probability of detection parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.pulse_integration_type`
              - Get or set the pulse integration type.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.pulse_integration`
              - Get the interface for setting pulse integration parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.enable_resolution_override`
              - Get or set the flag for overriding the computed range and azimuth resolution values.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.range_cell_resolution`
              - Get or set the overriding range cell resolution value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.azimuth_resolution`
              - Get or set the overriding azimuth resolution value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.enable_pulse_canceller`
              - Get or set the flag for enabling pulse cancellation.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.number_of_pulses_to_cancel`
              - Get or set the number of pulses to cancel.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.enable_coherent_pulses`
              - Get or set the flag for modeling coherent pulses.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarWaveformMonostaticSearchTrackFixedPRF


Property detail
---------------

.. py:property:: pulse_definition
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.pulse_definition
    :type: RadarWaveformSearchTrackPulseDefinition

    Get the interface for setting the pulse definition parameters.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.modulator
    :type: RadarModulator

    Get the interface for setting the modulator parameters.

.. py:property:: supported_probability_of_detection
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.supported_probability_of_detection
    :type: list

    Get an array of supported model names.

.. py:property:: probability_of_detection
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.probability_of_detection
    :type: IRadarProbabilityOfDetection

    Get the interface for setting the probability of detection parameters.

.. py:property:: pulse_integration_type
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.pulse_integration_type
    :type: RadarPulseIntegrationType

    Get or set the pulse integration type.

.. py:property:: pulse_integration
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.pulse_integration
    :type: IRadarPulseIntegration

    Get the interface for setting pulse integration parameters.

.. py:property:: enable_resolution_override
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.enable_resolution_override
    :type: bool

    Get or set the flag for overriding the computed range and azimuth resolution values.

.. py:property:: range_cell_resolution
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.range_cell_resolution
    :type: float

    Get or set the overriding range cell resolution value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.azimuth_resolution
    :type: float

    Get or set the overriding azimuth resolution value.

.. py:property:: enable_pulse_canceller
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.enable_pulse_canceller
    :type: bool

    Get or set the flag for enabling pulse cancellation.

.. py:property:: number_of_pulses_to_cancel
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.number_of_pulses_to_cancel
    :type: int

    Get or set the number of pulses to cancel.

.. py:property:: enable_coherent_pulses
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.enable_coherent_pulses
    :type: bool

    Get or set the flag for modeling coherent pulses.


Method detail
-------------




.. py:method:: set_probability_of_detection(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF.set_probability_of_detection

    Set the probability of detection algorithm by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

















