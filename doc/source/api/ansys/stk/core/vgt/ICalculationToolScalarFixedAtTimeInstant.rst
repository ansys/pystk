ICalculationToolScalarFixedAtTimeInstant
========================================

.. py:class:: ICalculationToolScalarFixedAtTimeInstant

   object
   
   Constant scalar created by evaluating the input scalar calculation at the specified reference time instant. Undefined if original scalar is not available at specified time or if reference time instant is undefined.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~input_scalar`
            * - :py:meth:`~reference_time_instant`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarFixedAtTimeInstant


Property detail
---------------

.. py:property:: input_scalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFixedAtTimeInstant.input_scalar
    :type: IAgCrdnCalcScalar

    The input scalar component.

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarFixedAtTimeInstant.reference_time_instant
    :type: IAgCrdnEvent

    The reference time instant.


