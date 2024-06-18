IEngineDefinition
=================

.. py:class:: IEngineDefinition

   object
   
   Properties for engine definition for an Ion engine model.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~isp_c0`
            * - :py:meth:`~isp_c1`
            * - :py:meth:`~isp_c2`
            * - :py:meth:`~isp_c3`
            * - :py:meth:`~mass_flow_rate_equation_type`
            * - :py:meth:`~mass_flow_rate_c0`
            * - :py:meth:`~mass_flow_rate_c1`
            * - :py:meth:`~mass_flow_rate_c2`
            * - :py:meth:`~mass_flow_rate_c3`
            * - :py:meth:`~mass_flow_rate_equation`
            * - :py:meth:`~mass_flow_efficiency_c0`
            * - :py:meth:`~mass_flow_efficiency_c1`
            * - :py:meth:`~mass_flow_efficiency_c2`
            * - :py:meth:`~mass_flow_efficiency_c3`
            * - :py:meth:`~mass_flow_efficiency_independent_var`
            * - :py:meth:`~mass_flow_efficiency_equation`
            * - :py:meth:`~power_efficiency_c0`
            * - :py:meth:`~power_efficiency_c1`
            * - :py:meth:`~power_efficiency_c2`
            * - :py:meth:`~power_efficiency_c3`
            * - :py:meth:`~power_efficiency_independent_var`
            * - :py:meth:`~power_efficiency_equation`
            * - :py:meth:`~input_power_source_name`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IEngineDefinition


Property detail
---------------

.. py:property:: isp_c0
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.isp_c0
    :type: float

    Gets or sets the constant coefficient (C0). Dimensionless.

.. py:property:: isp_c1
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.isp_c1
    :type: float

    Gets or sets the linear coefficient (C1). Dimensionless.

.. py:property:: isp_c2
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.isp_c2
    :type: float

    Gets or sets the quadratic coefficient (C2). Dimensionless.

.. py:property:: isp_c3
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.isp_c3
    :type: float

    Gets or sets the cubic coefficient (C3). Dimensionless.

.. py:property:: mass_flow_rate_equation_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_rate_equation_type
    :type: "ENGINE_MODEL_FUNCTION"

    Gets or sets the independent variable for the mass flow rate equation.

.. py:property:: mass_flow_rate_c0
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_rate_c0
    :type: float

    Gets or sets the constant coefficient (C0). Dimensionless.

.. py:property:: mass_flow_rate_c1
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_rate_c1
    :type: float

    Gets or sets the linear coefficient (C1). Dimensionless.

.. py:property:: mass_flow_rate_c2
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_rate_c2
    :type: float

    Gets or sets the quadratic coefficient (C2). Dimensionless.

.. py:property:: mass_flow_rate_c3
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_rate_c3
    :type: float

    Gets or sets the cubic coefficient (C3). Dimensionless.

.. py:property:: mass_flow_rate_equation
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_rate_equation
    :type: str

    Get the equation for mass flow rate.

.. py:property:: mass_flow_efficiency_c0
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_efficiency_c0
    :type: float

    Gets or sets the constant coefficient (C0). Dimensionless.

.. py:property:: mass_flow_efficiency_c1
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_efficiency_c1
    :type: float

    Gets or sets the linear coefficient (C1). Dimensionless.

.. py:property:: mass_flow_efficiency_c2
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_efficiency_c2
    :type: float

    Gets or sets the quadratic coefficient (C2). Dimensionless.

.. py:property:: mass_flow_efficiency_c3
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_efficiency_c3
    :type: float

    Gets or sets the cubic coefficient (C3). Dimensionless.

.. py:property:: mass_flow_efficiency_independent_var
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_efficiency_independent_var
    :type: "ENGINE_MODEL_FUNCTION"

    Gets or sets the independent variable for the mass flow efficiency equation.

.. py:property:: mass_flow_efficiency_equation
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.mass_flow_efficiency_equation
    :type: str

    Get the equation for mass flow efficiency.

.. py:property:: power_efficiency_c0
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.power_efficiency_c0
    :type: float

    Gets or sets the constant coefficient (C0). Dimensionless.

.. py:property:: power_efficiency_c1
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.power_efficiency_c1
    :type: float

    Gets or sets the linear coefficient (C1). Dimensionless.

.. py:property:: power_efficiency_c2
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.power_efficiency_c2
    :type: float

    Gets or sets the quadratic coefficient (C2). Dimensionless.

.. py:property:: power_efficiency_c3
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.power_efficiency_c3
    :type: float

    Gets or sets the cubic coefficient (C3). Dimensionless.

.. py:property:: power_efficiency_independent_var
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.power_efficiency_independent_var
    :type: "ENGINE_MODEL_FUNCTION"

    Gets or sets the independent variable for the power efficiency equation.

.. py:property:: power_efficiency_equation
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.power_efficiency_equation
    :type: str

    Get the equation for power efficiency.

.. py:property:: input_power_source_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineDefinition.input_power_source_name
    :type: str

    Object that computes the power input to the engine.


