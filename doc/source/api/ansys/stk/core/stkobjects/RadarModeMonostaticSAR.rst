RadarModeMonostaticSAR
======================

.. py:class:: ansys.stk.core.stkobjects.RadarModeMonostaticSAR

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModeMonostatic`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a monostatic sar radar mode.

.. py:currentmodule:: RadarModeMonostaticSAR

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeMonostaticSAR.pulse_definition`
              - Get the interface for configuring the SAR waveform pulse definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeMonostaticSAR.modulator`
              - Get the interface for setting the modulator parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeMonostaticSAR.pulse_integration`
              - Get the interface for configuring the SAR waveform pulse integration.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModeMonostaticSAR


Property detail
---------------

.. py:property:: pulse_definition
    :canonical: ansys.stk.core.stkobjects.RadarModeMonostaticSAR.pulse_definition
    :type: RadarWaveformSarPulseDefinition

    Get the interface for configuring the SAR waveform pulse definition.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.RadarModeMonostaticSAR.modulator
    :type: RadarModulator

    Get the interface for setting the modulator parameters.

.. py:property:: pulse_integration
    :canonical: ansys.stk.core.stkobjects.RadarModeMonostaticSAR.pulse_integration
    :type: RadarWaveformSarPulseIntegration

    Get the interface for configuring the SAR waveform pulse integration.


