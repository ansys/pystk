IRadarWaveformMonostaticSearchTrackFixedPRF
===========================================

.. py:class:: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF

   object
   
   Interface which is implemented by a search/track waveform.

.. py:currentmodule:: IRadarWaveformMonostaticSearchTrackFixedPRF

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.set_probability_of_detection`
              - Set the probability of detection algorithm by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.pulse_definition`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.modulator`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.supported_probability_of_detection`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.probability_of_detection`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.pulse_integration_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.pulse_integration`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.enable_resolution_override`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.range_cell_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.azimuth_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.enable_pulse_canceller`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.number_of_pulses_to_cancel`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.enable_coherent_pulses`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarWaveformMonostaticSearchTrackFixedPRF


Property detail
---------------

.. py:property:: pulse_definition
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.pulse_definition
    :type: IRadarWaveformSearchTrackPulseDefinition

    Gets the interface for setting the pulse definition parameters.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.modulator
    :type: IRadarModulator

    Gets the interface for setting the modulator parameters.

.. py:property:: supported_probability_of_detection
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.supported_probability_of_detection
    :type: list

    Gets an array of supported model names.

.. py:property:: probability_of_detection
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.probability_of_detection
    :type: IRadarProbabilityOfDetection

    Gets the interface for setting the probability of detection parameters.

.. py:property:: pulse_integration_type
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.pulse_integration_type
    :type: RADAR_PULSE_INTEGRATION_TYPE

    Gets or sets the pulse integration type.

.. py:property:: pulse_integration
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.pulse_integration
    :type: IRadarPulseIntegration

    Gets the interface for setting pulse integration parameters.

.. py:property:: enable_resolution_override
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.enable_resolution_override
    :type: bool

    Gets or sets the flag for overriding the computed range and azimuth resolution values.

.. py:property:: range_cell_resolution
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.range_cell_resolution
    :type: float

    Gets or sets the overriding range cell resolution value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.azimuth_resolution
    :type: float

    Gets or sets the overriding azimuth resolution value.

.. py:property:: enable_pulse_canceller
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.enable_pulse_canceller
    :type: bool

    Gets or sets the flag for enabling pulse cancellation.

.. py:property:: number_of_pulses_to_cancel
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.number_of_pulses_to_cancel
    :type: int

    Gets or sets the number of pulses to cancel.

.. py:property:: enable_coherent_pulses
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.enable_coherent_pulses
    :type: bool

    Gets or sets the flag for modeling coherent pulses.


Method detail
-------------




.. py:method:: set_probability_of_detection(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformMonostaticSearchTrackFixedPRF.set_probability_of_detection

    Set the probability of detection algorithm by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

















