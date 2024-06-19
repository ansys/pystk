IRadarModeBistaticTransmitterSar
================================

.. py:class:: IRadarModeBistaticTransmitterSar

   object
   
   Provide access to the properties and methods defining a bistatic transmitter sar mode.

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

    from ansys.stk.core.stkobjects import IRadarModeBistaticTransmitterSar


Property detail
---------------

.. py:property:: pulse_definition
    :canonical: ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSar.pulse_definition
    :type: IAgRadarWaveformSarPulseDefinition

    Gets the interface for configuring the SAR waveform pulse definition.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSar.modulator
    :type: IAgRadarModulator

    Gets the interface for setting the modulator parameters.


