CalculationToolScalarFixedAtTimeInstant
=======================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarFixedAtTimeInstant

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Constant scalar created by evaluating the input scalar calculation at the specified reference time instant. Undefined if original scalar is not available at specified time or if reference time instant is undefined.

.. py:currentmodule:: CalculationToolScalarFixedAtTimeInstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFixedAtTimeInstant.input_scalar`
              - The input scalar component.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFixedAtTimeInstant.reference_time_instant`
              - The reference time instant.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarFixedAtTimeInstant


Property detail
---------------

.. py:property:: input_scalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFixedAtTimeInstant.input_scalar
    :type: ICalculationToolScalar

    The input scalar component.

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarFixedAtTimeInstant.reference_time_instant
    :type: ITimeToolInstant

    The reference time instant.


