EngineDefinition
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.EngineDefinition

   Engine definition.

.. py:currentmodule:: EngineDefinition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.isp_c0`
              - Get or set the constant coefficient (C0). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.isp_c1`
              - Get or set the linear coefficient (C1). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.isp_c2`
              - Get or set the quadratic coefficient (C2). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.isp_c3`
              - Get or set the cubic coefficient (C3). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_equation_type`
              - Get or set the independent variable for the mass flow rate equation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_c0`
              - Get or set the constant coefficient (C0). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_c1`
              - Get or set the linear coefficient (C1). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_c2`
              - Get or set the quadratic coefficient (C2). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_c3`
              - Get or set the cubic coefficient (C3). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_equation`
              - Get the equation for mass flow rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_c0`
              - Get or set the constant coefficient (C0). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_c1`
              - Get or set the linear coefficient (C1). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_c2`
              - Get or set the quadratic coefficient (C2). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_c3`
              - Get or set the cubic coefficient (C3). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_independent_var`
              - Get or set the independent variable for the mass flow efficiency equation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_equation`
              - Get the equation for mass flow efficiency.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_c0`
              - Get or set the constant coefficient (C0). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_c1`
              - Get or set the linear coefficient (C1). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_c2`
              - Get or set the quadratic coefficient (C2). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_c3`
              - Get or set the cubic coefficient (C3). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_independent_var`
              - Get or set the independent variable for the power efficiency equation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_equation`
              - Get the equation for power efficiency.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition.input_power_source_name`
              - Object that computes the power input to the engine.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import EngineDefinition


Property detail
---------------

.. py:property:: isp_c0
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.isp_c0
    :type: float

    Get or set the constant coefficient (C0). Dimensionless.

.. py:property:: isp_c1
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.isp_c1
    :type: float

    Get or set the linear coefficient (C1). Dimensionless.

.. py:property:: isp_c2
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.isp_c2
    :type: float

    Get or set the quadratic coefficient (C2). Dimensionless.

.. py:property:: isp_c3
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.isp_c3
    :type: float

    Get or set the cubic coefficient (C3). Dimensionless.

.. py:property:: mass_flow_rate_equation_type
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_equation_type
    :type: EngineModelFunction

    Get or set the independent variable for the mass flow rate equation.

.. py:property:: mass_flow_rate_c0
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_c0
    :type: float

    Get or set the constant coefficient (C0). Dimensionless.

.. py:property:: mass_flow_rate_c1
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_c1
    :type: float

    Get or set the linear coefficient (C1). Dimensionless.

.. py:property:: mass_flow_rate_c2
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_c2
    :type: float

    Get or set the quadratic coefficient (C2). Dimensionless.

.. py:property:: mass_flow_rate_c3
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_c3
    :type: float

    Get or set the cubic coefficient (C3). Dimensionless.

.. py:property:: mass_flow_rate_equation
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_rate_equation
    :type: str

    Get the equation for mass flow rate.

.. py:property:: mass_flow_efficiency_c0
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_c0
    :type: float

    Get or set the constant coefficient (C0). Dimensionless.

.. py:property:: mass_flow_efficiency_c1
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_c1
    :type: float

    Get or set the linear coefficient (C1). Dimensionless.

.. py:property:: mass_flow_efficiency_c2
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_c2
    :type: float

    Get or set the quadratic coefficient (C2). Dimensionless.

.. py:property:: mass_flow_efficiency_c3
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_c3
    :type: float

    Get or set the cubic coefficient (C3). Dimensionless.

.. py:property:: mass_flow_efficiency_independent_var
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_independent_var
    :type: EngineModelFunction

    Get or set the independent variable for the mass flow efficiency equation.

.. py:property:: mass_flow_efficiency_equation
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.mass_flow_efficiency_equation
    :type: str

    Get the equation for mass flow efficiency.

.. py:property:: power_efficiency_c0
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_c0
    :type: float

    Get or set the constant coefficient (C0). Dimensionless.

.. py:property:: power_efficiency_c1
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_c1
    :type: float

    Get or set the linear coefficient (C1). Dimensionless.

.. py:property:: power_efficiency_c2
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_c2
    :type: float

    Get or set the quadratic coefficient (C2). Dimensionless.

.. py:property:: power_efficiency_c3
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_c3
    :type: float

    Get or set the cubic coefficient (C3). Dimensionless.

.. py:property:: power_efficiency_independent_var
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_independent_var
    :type: EngineModelFunction

    Get or set the independent variable for the power efficiency equation.

.. py:property:: power_efficiency_equation
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.power_efficiency_equation
    :type: str

    Get the equation for power efficiency.

.. py:property:: input_power_source_name
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineDefinition.input_power_source_name
    :type: str

    Object that computes the power input to the engine.


