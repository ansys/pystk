RadarModeMonostaticSar
======================

.. py:class:: ansys.stk.core.stkobjects.RadarModeMonostaticSar

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModeMonostatic`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a monostatic sar radar mode.

.. py:currentmodule:: RadarModeMonostaticSar

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeMonostaticSar.pulse_definition`
              - Gets the interface for configuring the SAR waveform pulse definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeMonostaticSar.modulator`
              - Gets the interface for setting the modulator parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeMonostaticSar.pulse_integration`
              - Gets the interface for configuring the SAR waveform pulse integration.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModeMonostaticSar


Property detail
---------------

.. py:property:: pulse_definition
    :canonical: ansys.stk.core.stkobjects.RadarModeMonostaticSar.pulse_definition
    :type: IRadarWaveformSarPulseDefinition

    Gets the interface for configuring the SAR waveform pulse definition.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.RadarModeMonostaticSar.modulator
    :type: IRadarModulator

    Gets the interface for setting the modulator parameters.

.. py:property:: pulse_integration
    :canonical: ansys.stk.core.stkobjects.RadarModeMonostaticSar.pulse_integration
    :type: IRadarWaveformSarPulseIntegration

    Gets the interface for configuring the SAR waveform pulse integration.


