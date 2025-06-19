VectorGeometryToolVectorLinearCombination
=========================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`

   Linear combination of two input vectors.

.. py:currentmodule:: VectorGeometryToolVectorLinearCombination

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.vector_a`
              - Vector A can be any VGT vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.scale_factor_a`
              - Scale factor for vector A.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.normalize_vector_a`
              - Whether to normalize vector A.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.vector_b`
              - Vector B can be any VGT vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.scale_factor_b`
              - Scale factor for vector B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.normalize_vector_b`
              - Whether to normalize vector B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.output_dimension_inheritance`
              - Determine whether the output dimension is inherited or explicitly specified using OutputDimension.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.output_dimension`
              - A dimension to interpret the output vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorLinearCombination


Property detail
---------------

.. py:property:: vector_a
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.vector_a
    :type: IVectorGeometryToolVector

    Vector A can be any VGT vector.

.. py:property:: scale_factor_a
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.scale_factor_a
    :type: float

    Scale factor for vector A.

.. py:property:: normalize_vector_a
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.normalize_vector_a
    :type: bool

    Whether to normalize vector A.

.. py:property:: vector_b
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.vector_b
    :type: IVectorGeometryToolVector

    Vector B can be any VGT vector.

.. py:property:: scale_factor_b
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.scale_factor_b
    :type: float

    Scale factor for vector B.

.. py:property:: normalize_vector_b
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.normalize_vector_b
    :type: bool

    Whether to normalize vector B.

.. py:property:: output_dimension_inheritance
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.output_dimension_inheritance
    :type: InheritDimensionType

    Determine whether the output dimension is inherited or explicitly specified using OutputDimension.

.. py:property:: output_dimension
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination.output_dimension
    :type: str

    A dimension to interpret the output vector.


