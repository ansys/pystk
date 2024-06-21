IRadarModeMonostaticSar
=======================

.. py:class:: ansys.stk.core.stkobjects.IRadarModeMonostaticSar

   object
   
   Provide access to the properties and methods defining a monostatic sar mode.

.. py:currentmodule:: IRadarModeMonostaticSar

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModeMonostaticSar.pulse_definition`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModeMonostaticSar.modulator`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModeMonostaticSar.pulse_integration`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarModeMonostaticSar


Property detail
---------------

.. py:property:: pulse_definition
    :canonical: ansys.stk.core.stkobjects.IRadarModeMonostaticSar.pulse_definition
    :type: IRadarWaveformSarPulseDefinition

    Gets the interface for configuring the SAR waveform pulse definition.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.IRadarModeMonostaticSar.modulator
    :type: IRadarModulator

    Gets the interface for setting the modulator parameters.

.. py:property:: pulse_integration
    :canonical: ansys.stk.core.stkobjects.IRadarModeMonostaticSar.pulse_integration
    :type: IRadarWaveformSarPulseIntegration

    Gets the interface for configuring the SAR waveform pulse integration.


