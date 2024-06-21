ICalculationToolDerivativeBasic
===============================

.. py:class:: ansys.stk.core.vgt.ICalculationToolDerivativeBasic

   object
   
   Derivative definition determines how numerical differencing is used to compute derivatives.

.. py:currentmodule:: ICalculationToolDerivativeBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolDerivativeBasic.time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolDerivativeBasic


Property detail
---------------

.. py:property:: time_step
    :canonical: ansys.stk.core.vgt.ICalculationToolDerivativeBasic.time_step
    :type: float

    Get the time step used for numerical evaluation of derivatives using central differencing.


