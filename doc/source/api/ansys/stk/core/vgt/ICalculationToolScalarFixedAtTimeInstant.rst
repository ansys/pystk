ICalculationToolScalarFixedAtTimeInstant
========================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolScalarFixedAtTimeInstant

   object
   
   Constant scalar created by evaluating the input scalar calculation at the specified reference time instant. Undefined if original scalar is not available at specified time or if reference time instant is undefined.

.. py:currentmodule:: ICalculationToolScalarFixedAtTimeInstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFixedAtTimeInstant.input_scalar`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarFixedAtTimeInstant.reference_time_instant`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarFixedAtTimeInstant


Property detail
---------------

.. py:property:: input_scalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFixedAtTimeInstant.input_scalar
    :type: ICalculationToolScalar

    The input scalar component.

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFixedAtTimeInstant.reference_time_instant
    :type: ITimeToolEvent

    The reference time instant.


