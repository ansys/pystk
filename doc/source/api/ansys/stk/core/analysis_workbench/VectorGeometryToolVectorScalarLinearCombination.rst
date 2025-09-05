VectorGeometryToolVectorScalarLinearCombination
===============================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`

   Linear combination of two input vectors using scalars.

.. py:currentmodule:: VectorGeometryToolVectorScalarLinearCombination

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.normalize_vector_a`
              - Whether to normalize vector A.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.normalize_vector_b`
              - Whether to normalize vector B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.output_dimension`
              - A dimension to interpret the output vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.output_dimension_inheritance`
              - Determine whether the output dimension is inherited or explicitly specified using OutputDimension.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.scalar_a`
              - Scalar scale A. Can be any Scalar calculation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.scalar_b`
              - Scalar scale B. Can be any Scalar calculation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.scale_factor_a`
              - Scale factor for vector A.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.scale_factor_b`
              - Scale factor for vector B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.use_scale_from_calculation_scalar_a`
              - Whether to use a scale from scalar A.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.use_scale_from_calculation_scalar_b`
              - Whether to use a scale from scalar B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.vector_a`
              - Vector A can be any VGT vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.vector_b`
              - Vector B can be any VGT vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorScalarLinearCombination


Property detail
---------------

.. py:property:: normalize_vector_a
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.normalize_vector_a
    :type: bool

    Whether to normalize vector A.

.. py:property:: normalize_vector_b
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.normalize_vector_b
    :type: bool

    Whether to normalize vector B.

.. py:property:: output_dimension
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.output_dimension
    :type: str

    A dimension to interpret the output vector.

.. py:property:: output_dimension_inheritance
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.output_dimension_inheritance
    :type: InheritDimensionType

    Determine whether the output dimension is inherited or explicitly specified using OutputDimension.

.. py:property:: scalar_a
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.scalar_a
    :type: ICalculationToolScalar

    Scalar scale A. Can be any Scalar calculation.

.. py:property:: scalar_b
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.scalar_b
    :type: ICalculationToolScalar

    Scalar scale B. Can be any Scalar calculation.

.. py:property:: scale_factor_a
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.scale_factor_a
    :type: float

    Scale factor for vector A.

.. py:property:: scale_factor_b
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.scale_factor_b
    :type: float

    Scale factor for vector B.

.. py:property:: use_scale_from_calculation_scalar_a
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.use_scale_from_calculation_scalar_a
    :type: bool

    Whether to use a scale from scalar A.

.. py:property:: use_scale_from_calculation_scalar_b
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.use_scale_from_calculation_scalar_b
    :type: bool

    Whether to use a scale from scalar B.

.. py:property:: vector_a
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.vector_a
    :type: IVectorGeometryToolVector

    Vector A can be any VGT vector.

.. py:property:: vector_b
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination.vector_b
    :type: IVectorGeometryToolVector

    Vector B can be any VGT vector.


