CalculationToolScalarConstant
=============================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarConstant

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Constant scalar value of specified dimension.

.. py:currentmodule:: CalculationToolScalarConstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarConstant.value`
              - A value which can be in any STK supported unit available for selected dimension.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarConstant.dimension`
              - The dimension of the constant value, this can be any of the STK supported dimensions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarConstant


Property detail
---------------

.. py:property:: value
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarConstant.value
    :type: float

    A value which can be in any STK supported unit available for selected dimension.

.. py:property:: dimension
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarConstant.dimension
    :type: str

    The dimension of the constant value, this can be any of the STK supported dimensions.


