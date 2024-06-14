IRadarPulseIntegrationGoalSNR
=============================

.. py:class:: IRadarPulseIntegrationGoalSNR

   object
   
   Interface which defines a goal SNR integration method.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~snr`
            * - :py:meth:`~maximum_pulses`
            * - :py:meth:`~integrator_type`
            * - :py:meth:`~constant_efficiency`
            * - :py:meth:`~exponent_on_pulse_number`
            * - :py:meth:`~integration_file`
            * - :py:meth:`~non_coherent_integration`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarPulseIntegrationGoalSNR


Property detail
---------------

.. py:property:: snr
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationGoalSNR.snr
    :type: float

    Gets or sets the goal SNR value.

.. py:property:: maximum_pulses
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationGoalSNR.maximum_pulses
    :type: int

    Gets or sets the maximum number of pulses.

.. py:property:: integrator_type
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationGoalSNR.integrator_type
    :type: "RADAR_PULSE_INTEGRATOR_TYPE"

    Gets or sets the integrator type.

.. py:property:: constant_efficiency
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationGoalSNR.constant_efficiency
    :type: float

    Gets or sets the constant efficiency value.

.. py:property:: exponent_on_pulse_number
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationGoalSNR.exponent_on_pulse_number
    :type: float

    Gets or sets the exponent on pulse number value.

.. py:property:: integration_file
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationGoalSNR.integration_file
    :type: str

    Gets or sets the integration file.

.. py:property:: non_coherent_integration
    :canonical: ansys.stk.core.stkobjects.IRadarPulseIntegrationGoalSNR.non_coherent_integration
    :type: bool

    Gets or sets the non-coherent integration flag.


