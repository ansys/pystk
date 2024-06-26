IRadarWaveformBistaticReceiverSearchTrackFixedPRF
=================================================

.. py:class:: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF

   object
   
   Interface which is implemented by a search/track waveform.

.. py:currentmodule:: IRadarWaveformBistaticReceiverSearchTrackFixedPRF

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.set_probability_of_detection`
              - Set the probability of detection algorithm by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.supported_probability_of_detection`
              - Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.probability_of_detection`
              - Gets the interface for setting the probability of detection parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.pulse_integration_type`
              - Gets or sets the pulse integration type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.pulse_integration`
              - Gets the interface for setting pulse integration parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_resolution_override`
              - Gets or sets the flag for overriding the computed range and azimuth resolution values.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.range_cell_resolution`
              - Gets or sets the overriding range cell resolution value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.azimuth_resolution`
              - Gets or sets the overriding azimuth resolution value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_pulse_canceller`
              - Gets or sets the flag for enabling pulse cancellation.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.number_of_pulses_to_cancel`
              - Gets or sets the number of pulses to cancel.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_coherent_pulses`
              - Gets or sets the flag for modeling coherent pulses.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarWaveformBistaticReceiverSearchTrackFixedPRF


Property detail
---------------

.. py:property:: supported_probability_of_detection
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.supported_probability_of_detection
    :type: list

    Gets an array of supported model names.

.. py:property:: probability_of_detection
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.probability_of_detection
    :type: IRadarProbabilityOfDetection

    Gets the interface for setting the probability of detection parameters.

.. py:property:: pulse_integration_type
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.pulse_integration_type
    :type: RADAR_PULSE_INTEGRATION_TYPE

    Gets or sets the pulse integration type.

.. py:property:: pulse_integration
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.pulse_integration
    :type: IRadarPulseIntegration

    Gets the interface for setting pulse integration parameters.

.. py:property:: enable_resolution_override
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_resolution_override
    :type: bool

    Gets or sets the flag for overriding the computed range and azimuth resolution values.

.. py:property:: range_cell_resolution
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.range_cell_resolution
    :type: float

    Gets or sets the overriding range cell resolution value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.azimuth_resolution
    :type: float

    Gets or sets the overriding azimuth resolution value.

.. py:property:: enable_pulse_canceller
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_pulse_canceller
    :type: bool

    Gets or sets the flag for enabling pulse cancellation.

.. py:property:: number_of_pulses_to_cancel
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.number_of_pulses_to_cancel
    :type: int

    Gets or sets the number of pulses to cancel.

.. py:property:: enable_coherent_pulses
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_coherent_pulses
    :type: bool

    Gets or sets the flag for modeling coherent pulses.


Method detail
-------------



.. py:method:: set_probability_of_detection(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticReceiverSearchTrackFixedPRF.set_probability_of_detection

    Set the probability of detection algorithm by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`
















