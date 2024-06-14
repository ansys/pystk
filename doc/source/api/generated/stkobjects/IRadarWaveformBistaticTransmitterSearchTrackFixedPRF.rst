IRadarWaveformBistaticTransmitterSearchTrackFixedPRF
====================================================

.. py:class:: IRadarWaveformBistaticTransmitterSearchTrackFixedPRF

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

            * - :py:meth:`~pulse_definition`
            * - :py:meth:`~modulator`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarWaveformBistaticTransmitterSearchTrackFixedPRF


Property detail
---------------

.. py:property:: pulse_definition
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticTransmitterSearchTrackFixedPRF.pulse_definition
    :type: "IAgRadarWaveformSearchTrackPulseDefinition"

    Gets the interface for setting the pulse definition parameters.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformBistaticTransmitterSearchTrackFixedPRF.modulator
    :type: "IAgRadarModulator"

    Gets the interface for setting the modulator parameters.


