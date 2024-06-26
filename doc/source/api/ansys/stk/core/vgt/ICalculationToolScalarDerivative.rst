ICalculationToolScalarDerivative
================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolScalarDerivative

   object
   
   Derivative of an input scalar calculation.

.. py:currentmodule:: ICalculationToolScalarDerivative

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDerivative.scalar`
              - The input scalar component used to compute the derivative.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDerivative.differencing_time_step`
              - The time step used, if necessary, in numerical evaluation of derivatives using central differencing.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDerivative.force_use_of_numerical_differences`
              - Force the use of numerical differences even if the derivative can be computed analytically.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarDerivative


Property detail
---------------

.. py:property:: scalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDerivative.scalar
    :type: ICalculationToolScalar

    The input scalar component used to compute the derivative.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDerivative.differencing_time_step
    :type: float

    The time step used, if necessary, in numerical evaluation of derivatives using central differencing.

.. py:property:: force_use_of_numerical_differences
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDerivative.force_use_of_numerical_differences
    :type: bool

    Force the use of numerical differences even if the derivative can be computed analytically.


