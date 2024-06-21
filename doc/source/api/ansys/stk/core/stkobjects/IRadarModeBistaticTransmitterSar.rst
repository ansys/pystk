IRadarModeBistaticTransmitterSar
================================

.. py:class:: ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSar

   object
   
   Provide access to the properties and methods defining a bistatic transmitter sar mode.

.. py:currentmodule:: IRadarModeBistaticTransmitterSar

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSar.pulse_definition`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSar.modulator`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarModeBistaticTransmitterSar


Property detail
---------------

.. py:property:: pulse_definition
    :canonical: ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSar.pulse_definition
    :type: IRadarWaveformSarPulseDefinition

    Gets the interface for configuring the SAR waveform pulse definition.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSar.modulator
    :type: IRadarModulator

    Gets the interface for setting the modulator parameters.


