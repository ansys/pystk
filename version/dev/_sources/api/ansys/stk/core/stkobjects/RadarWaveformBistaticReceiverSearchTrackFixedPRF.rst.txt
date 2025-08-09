RadarWaveformBistaticReceiverSearchTrackFixedPRF
================================================

.. py:class:: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarWaveformSearchTrack`

   Class defining a bistatic receiver fixed PRF waveform.

.. py:currentmodule:: RadarWaveformBistaticReceiverSearchTrackFixedPRF

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.set_probability_of_detection`
              - Set the probability of detection algorithm by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.azimuth_resolution`
              - Get or set the overriding azimuth resolution value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_coherent_pulses`
              - Get or set the flag for modeling coherent pulses.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_pulse_canceller`
              - Get or set the flag for enabling pulse cancellation.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_resolution_override`
              - Get or set the flag for overriding the computed range and azimuth resolution values.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.number_of_pulses_to_cancel`
              - Get or set the number of pulses to cancel.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.probability_of_detection`
              - Get the interface for setting the probability of detection parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.pulse_integration`
              - Get the interface for setting pulse integration parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.pulse_integration_type`
              - Get or set the pulse integration type.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.range_cell_resolution`
              - Get or set the overriding range cell resolution value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.supported_probability_of_detection`
              - Get an array of supported model names.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarWaveformBistaticReceiverSearchTrackFixedPRF


Property detail
---------------

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.azimuth_resolution
    :type: float

    Get or set the overriding azimuth resolution value.

.. py:property:: enable_coherent_pulses
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_coherent_pulses
    :type: bool

    Get or set the flag for modeling coherent pulses.

.. py:property:: enable_pulse_canceller
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_pulse_canceller
    :type: bool

    Get or set the flag for enabling pulse cancellation.

.. py:property:: enable_resolution_override
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.enable_resolution_override
    :type: bool

    Get or set the flag for overriding the computed range and azimuth resolution values.

.. py:property:: number_of_pulses_to_cancel
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.number_of_pulses_to_cancel
    :type: int

    Get or set the number of pulses to cancel.

.. py:property:: probability_of_detection
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.probability_of_detection
    :type: IRadarProbabilityOfDetection

    Get the interface for setting the probability of detection parameters.

.. py:property:: pulse_integration
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.pulse_integration
    :type: IRadarPulseIntegration

    Get the interface for setting pulse integration parameters.

.. py:property:: pulse_integration_type
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.pulse_integration_type
    :type: RadarPulseIntegrationType

    Get or set the pulse integration type.

.. py:property:: range_cell_resolution
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.range_cell_resolution
    :type: float

    Get or set the overriding range cell resolution value.

.. py:property:: supported_probability_of_detection
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.supported_probability_of_detection
    :type: list

    Get an array of supported model names.


Method detail
-------------

















.. py:method:: set_probability_of_detection(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF.set_probability_of_detection

    Set the probability of detection algorithm by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`


