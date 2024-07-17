CalculationToolIntegralBasic
============================

.. py:class:: ansys.stk.core.vgt.CalculationToolIntegralBasic

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchIntegral`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Integral definition determines how scalar calculation is numerically integrated.

.. py:currentmodule:: CalculationToolIntegralBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolIntegralBasic.type`
              - Get the integral type which determines the method of integration and can be set to trapezoidal, Simplson or adaptive Lobatto.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolIntegralBasic.tolerance`
              - Get the tolerance which determines how accurate integral is computed by finding relative difference between refined and unrefined integral evaluations. Only available if Adaptive Lobatto is selected as the integral type.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolIntegralBasic.maximum_iterations`
              - Get the number of iteration which determines how many refinement iterations are allowed. Only available if Adaptive Lobatto is selected as the integral type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolIntegralBasic


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.CalculationToolIntegralBasic.type
    :type: CRDN_INTEGRAL_TYPE

    Get the integral type which determines the method of integration and can be set to trapezoidal, Simplson or adaptive Lobatto.

.. py:property:: tolerance
    :canonical: ansys.stk.core.vgt.CalculationToolIntegralBasic.tolerance
    :type: float

    Get the tolerance which determines how accurate integral is computed by finding relative difference between refined and unrefined integral evaluations. Only available if Adaptive Lobatto is selected as the integral type.

.. py:property:: maximum_iterations
    :canonical: ansys.stk.core.vgt.CalculationToolIntegralBasic.maximum_iterations
    :type: int

    Get the number of iteration which determines how many refinement iterations are allowed. Only available if Adaptive Lobatto is selected as the integral type.


