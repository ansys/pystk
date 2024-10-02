CalculationToolDerivativeBasic
==============================

.. py:class:: ansys.stk.core.vgt.CalculationToolDerivativeBasic

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchDerivative`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Derivative definition determines how numerical differencing is used to compute derivatives.

.. py:currentmodule:: CalculationToolDerivativeBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolDerivativeBasic.time_step`
              - Get the time step used for numerical evaluation of derivatives using central differencing.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolDerivativeBasic


Property detail
---------------

.. py:property:: time_step
    :canonical: ansys.stk.core.vgt.CalculationToolDerivativeBasic.time_step
    :type: float

    Get the time step used for numerical evaluation of derivatives using central differencing.


