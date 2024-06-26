CONTROL_ENGINE_ION
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CONTROL_ENGINE_ION

   IntEnum


.. py:currentmodule:: CONTROL_ENGINE_ION

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FLOW_RATE_C0`
              - FlowRateModel.C0 - the constant coefficient.

            * - :py:attr:`~FLOW_RATE_C1`
              - FlowRateModel.C1 - the linear coefficient.

            * - :py:attr:`~FLOW_RATE_C2`
              - FlowRateModel.C2 - the quadratic coefficient.

            * - :py:attr:`~FLOW_RATE_C3`
              - FlowRateModel.C3 - the cubic coefficient.

            * - :py:attr:`~GRAV`
              - Gravitational acceleration constant at sea level on the Earth.

            * - :py:attr:`~ISP_C0`
              - IspModel.C0 - the constant coefficient.

            * - :py:attr:`~ISP_C1`
              - IspModel.C1 - the linear coefficient.

            * - :py:attr:`~ISP_C2`
              - IspModel.C2 - the quadratic coefficient.

            * - :py:attr:`~ISP_C3`
              - IspModel.C3 - the cubic coefficient.

            * - :py:attr:`~MASS_FLOW_EFFICIENCY_C0`
              - MassFlowEfficiencyModel.C0 - the constant coefficient.

            * - :py:attr:`~MASS_FLOW_EFFICIENCY_C1`
              - MassFlowEfficiencyModel.C1 - the linear coefficient.

            * - :py:attr:`~MASS_FLOW_EFFICIENCY_C2`
              - MassFlowEfficiencyModel.C2 - the quadratic coefficient.

            * - :py:attr:`~MASS_FLOW_EFFICIENCY_C3`
              - MassFlowEfficiencyModel.C3 - the cubic coefficient.

            * - :py:attr:`~MAX_INPUT_POWER`
              - Minimum power required for the engine to produce thrust.

            * - :py:attr:`~MIN_REQUIRED_POWER`
              - Maximum power that can be used by the engine to produce thrust.

            * - :py:attr:`~PERCENT_DEGRADATION_PER_YEAR`
              - The degradation factor is (1 - x)n, where n is the time since epoch in years, and x is the percent degradation per year.

            * - :py:attr:`~PERCENT_THROTTLE`
              - Percentage of available thrust to use (100 is full on, 0 is off).

            * - :py:attr:`~POWER_EFFICIENCY_C0`
              - PowerEfficiencyModel.C0 - the constant coefficient.

            * - :py:attr:`~POWER_EFFICIENCY_C1`
              - PowerEfficiencyModel.C1 - the linear coefficient.

            * - :py:attr:`~POWER_EFFICIENCY_C2`
              - PowerEfficiencyModel.C2 - the quadratic coefficient.

            * - :py:attr:`~POWER_EFFICIENCY_C3`
              - PowerEfficiencyModel.C3 - the cubic coefficient.

            * - :py:attr:`~REFERENCE_EPOCH`
              - The date and time used as a reference epoch for degradation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CONTROL_ENGINE_ION


