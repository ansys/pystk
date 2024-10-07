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

            * - :py:attr:`~FLOW_RATE_CONSTANT_TERM`
              - FlowRateModel.C0 - the constant coefficient.

            * - :py:attr:`~FLOW_RATE_LINEAR_TERM`
              - FlowRateModel.C1 - the linear coefficient.

            * - :py:attr:`~FLOW_RATE_QUADRATIC_TERM`
              - FlowRateModel.C2 - the quadratic coefficient.

            * - :py:attr:`~FLOW_RATE_CUBIC_TERM`
              - FlowRateModel.C3 - the cubic coefficient.

            * - :py:attr:`~GRAV`
              - Gravitational acceleration constant at sea level on the Earth.

            * - :py:attr:`~ISP_CONSTANT_TERM`
              - IspModel.C0 - the constant coefficient.

            * - :py:attr:`~ISP_LINEAR_TERM`
              - IspModel.C1 - the linear coefficient.

            * - :py:attr:`~ISP_QUADRATIC_TERM`
              - IspModel.C2 - the quadratic coefficient.

            * - :py:attr:`~ISP_CUBIC_TERM`
              - IspModel.C3 - the cubic coefficient.

            * - :py:attr:`~MASS_FLOW_EFFICIENCY_CONSTANT_TERM`
              - MassFlowEfficiencyModel.C0 - the constant coefficient.

            * - :py:attr:`~MASS_FLOW_EFFICIENCY_LINEAR_TERM`
              - MassFlowEfficiencyModel.C1 - the linear coefficient.

            * - :py:attr:`~MASS_FLOW_EFFICIENCY_QUADRATIC_TERM`
              - MassFlowEfficiencyModel.C2 - the quadratic coefficient.

            * - :py:attr:`~MASS_FLOW_EFFICIENCY_CUBIC_TERM`
              - MassFlowEfficiencyModel.C3 - the cubic coefficient.

            * - :py:attr:`~MAX_INPUT_POWER`
              - Minimum power required for the engine to produce thrust.

            * - :py:attr:`~MIN_REQUIRED_POWER`
              - Maximum power that can be used by the engine to produce thrust.

            * - :py:attr:`~PERCENT_DEGRADATION_PER_YEAR`
              - The degradation factor is (1 - x)n, where n is the time since epoch in years, and x is the percent degradation per year.

            * - :py:attr:`~PERCENT_THROTTLE`
              - Percentage of available thrust to use (100 is full on, 0 is off).

            * - :py:attr:`~POWER_EFFICIENCY_CONSTANT_TERM`
              - PowerEfficiencyModel.C0 - the constant coefficient.

            * - :py:attr:`~POWER_EFFICIENCY_LINEAR_TERM`
              - PowerEfficiencyModel.C1 - the linear coefficient.

            * - :py:attr:`~POWER_EFFICIENCY_QUADRATIC_TERM`
              - PowerEfficiencyModel.C2 - the quadratic coefficient.

            * - :py:attr:`~POWER_EFFICIENCY_CUBIC_TERM`
              - PowerEfficiencyModel.C3 - the cubic coefficient.

            * - :py:attr:`~REFERENCE_EPOCH`
              - The date and time used as a reference epoch for degradation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CONTROL_ENGINE_ION


