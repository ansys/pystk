RadarModeBistaticTransmitterSar
===============================

.. py:class:: ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSar

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModeBistaticTransmitter`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a bistatic transmitter sar radar mode.

.. py:currentmodule:: RadarModeBistaticTransmitterSar

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSar.pulse_definition`
              - Gets the interface for configuring the SAR waveform pulse definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSar.modulator`
              - Gets the interface for setting the modulator parameters.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModeBistaticTransmitterSar


Property detail
---------------

.. py:property:: pulse_definition
    :canonical: ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSar.pulse_definition
    :type: IRadarWaveformSarPulseDefinition

    Gets the interface for configuring the SAR waveform pulse definition.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSar.modulator
    :type: IRadarModulator

    Gets the interface for setting the modulator parameters.


