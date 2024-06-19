ICalculationToolScalarDerivative
================================

.. py:class:: ICalculationToolScalarDerivative

   object
   
   Derivative of an input scalar calculation.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~scalar`
            * - :py:meth:`~differencing_time_step`
            * - :py:meth:`~force_use_of_numerical_differences`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarDerivative


Property detail
---------------

.. py:property:: scalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDerivative.scalar
    :type: IAgCrdnCalcScalar

    The input scalar component used to compute the derivative.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDerivative.differencing_time_step
    :type: float

    The time step used, if necessary, in numerical evaluation of derivatives using central differencing.

.. py:property:: force_use_of_numerical_differences
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDerivative.force_use_of_numerical_differences
    :type: bool

    Force the use of numerical differences even if the derivative can be computed analytically.


