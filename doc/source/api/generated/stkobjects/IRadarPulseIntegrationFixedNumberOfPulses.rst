IRadarPulseIntegrationFixedNumberOfPulses
=========================================

.. py:class:: IRadarPulseIntegrationFixedNumberOfPulses

   object
   
   Interface which defines a fixed number of pulses integration method.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~pulse_number`
            * - :py:meth:`~integrator_type`
            * - :py:meth:`~constant_efficiency`
            * - :py:meth:`~exponent_on_pulse_number`
            * - :py:meth:`~non_coherent_integration`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarPulseIntegrationFixedNumberOfPulses


Property detail
---------------

.. py:property:: pulse_number
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationFixedNumberOfPulses.pulse_number
    :type: int

    Gets or sets the pulse number.

.. py:property:: integrator_type
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationFixedNumberOfPulses.integrator_type
    :type: "RADAR_PULSE_INTEGRATOR_TYPE"

    Gets or sets the integrator type.

.. py:property:: constant_efficiency
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationFixedNumberOfPulses.constant_efficiency
    :type: float

    Gets or sets the constant efficiency value.

.. py:property:: exponent_on_pulse_number
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationFixedNumberOfPulses.exponent_on_pulse_number
    :type: float

    Gets or set the exponent on pulse number value.

.. py:property:: non_coherent_integration
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationFixedNumberOfPulses.non_coherent_integration
    :type: bool

    Gets or sets the non-coherent integration flag.


