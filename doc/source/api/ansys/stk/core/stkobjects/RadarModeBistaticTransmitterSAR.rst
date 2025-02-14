RadarModeBistaticTransmitterSAR
===============================

.. py:class:: ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSAR

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModeBistaticTransmitter`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a bistatic transmitter sar radar mode.

.. py:currentmodule:: RadarModeBistaticTransmitterSAR

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSAR.pulse_definition`
              - Get the interface for configuring the SAR waveform pulse definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSAR.modulator`
              - Get the interface for setting the modulator parameters.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModeBistaticTransmitterSAR


Property detail
---------------

.. py:property:: pulse_definition
    :canonical: ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSAR.pulse_definition
    :type: RadarWaveformSarPulseDefinition

    Get the interface for configuring the SAR waveform pulse definition.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSAR.modulator
    :type: RadarModulator

    Get the interface for setting the modulator parameters.


