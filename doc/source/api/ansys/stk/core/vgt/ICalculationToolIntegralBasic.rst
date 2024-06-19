ICalculationToolIntegralBasic
=============================

.. py:class:: ICalculationToolIntegralBasic

   object
   
   Integral definition determines how scalar calculation is numerically integrated.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~tolerance`
            * - :py:meth:`~maximum_iterations`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolIntegralBasic


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ICalculationToolIntegralBasic.type
    :type: CRDN_INTEGRAL_TYPE

    Get the integral type which determines the method of integration and can be set to trapezoidal, Simplson or adaptive Lobatto.

.. py:property:: tolerance
    :canonical: ansys.stk.core.vgt.ICalculationToolIntegralBasic.tolerance
    :type: float

    Get the tolerance which determines how accurate integral is computed by finding relative difference between refined and unrefined integral evaluations. Only available if Adaptive Lobatto is selected as the integral type.

.. py:property:: maximum_iterations
    :canonical: ansys.stk.core.vgt.ICalculationToolIntegralBasic.maximum_iterations
    :type: int

    Get the number of iteration which determines how many refinement iterations are allowed. Only available if Adaptive Lobatto is selected as the integral type.


