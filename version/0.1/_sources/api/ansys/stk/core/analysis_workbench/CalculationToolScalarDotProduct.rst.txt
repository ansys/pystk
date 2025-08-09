CalculationToolScalarDotProduct
===============================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Dot product between two vectors.

.. py:currentmodule:: CalculationToolScalarDotProduct

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct.vector_a`
              - First vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct.normalize_vector_a`
              - Whether to normalize vector A.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct.vector_b`
              - Second vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct.normalize_vector_b`
              - Whether to normalize vector B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct.dimension`
              - Return a unit of measure, i.e. 'Angle', 'Distance', etc.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarDotProduct


Property detail
---------------

.. py:property:: vector_a
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct.vector_a
    :type: IVectorGeometryToolVector

    First vector.

.. py:property:: normalize_vector_a
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct.normalize_vector_a
    :type: bool

    Whether to normalize vector A.

.. py:property:: vector_b
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct.vector_b
    :type: IVectorGeometryToolVector

    Second vector.

.. py:property:: normalize_vector_b
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct.normalize_vector_b
    :type: bool

    Whether to normalize vector B.

.. py:property:: dimension
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct.dimension
    :type: str

    Return a unit of measure, i.e. 'Angle', 'Distance', etc.


