IVectorGeometryToolVectorScalarLinearCombination
================================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination

   object
   
   Linear combination of two input vectors using scalars.

.. py:currentmodule:: IVectorGeometryToolVectorScalarLinearCombination

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.vector_a`
              - Vector A can be any VGT vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.scale_factor_a`
              - Scale factor for vector A.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.normalize_vector_a`
              - Whether to normalize vector A.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.use_scale_from_scalar_a`
              - Whether to use a scale from scalar A.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.use_scale_from_scalar_b`
              - Whether to use a scale from scalar B.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.scalar_a`
              - Scalar scale A. Can be any Scalar calculation.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.scalar_b`
              - Scalar scale B. Can be any Scalar calculation.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.vector_b`
              - Vector B can be any VGT vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.scale_factor_b`
              - Scale factor for vector B.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.normalize_vector_b`
              - Whether to normalize vector B.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.output_dimension_inheritance`
              - Determines whether the output dimension is inherited or explicitly specified using OutputDimension.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.output_dimension`
              - A dimension to interpret the output vector.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorScalarLinearCombination


Property detail
---------------

.. py:property:: vector_a
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.vector_a
    :type: IVectorGeometryToolVector

    Vector A can be any VGT vector.

.. py:property:: scale_factor_a
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.scale_factor_a
    :type: float

    Scale factor for vector A.

.. py:property:: normalize_vector_a
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.normalize_vector_a
    :type: bool

    Whether to normalize vector A.

.. py:property:: use_scale_from_scalar_a
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.use_scale_from_scalar_a
    :type: bool

    Whether to use a scale from scalar A.

.. py:property:: use_scale_from_scalar_b
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.use_scale_from_scalar_b
    :type: bool

    Whether to use a scale from scalar B.

.. py:property:: scalar_a
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.scalar_a
    :type: ICalculationToolScalar

    Scalar scale A. Can be any Scalar calculation.

.. py:property:: scalar_b
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.scalar_b
    :type: ICalculationToolScalar

    Scalar scale B. Can be any Scalar calculation.

.. py:property:: vector_b
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.vector_b
    :type: IVectorGeometryToolVector

    Vector B can be any VGT vector.

.. py:property:: scale_factor_b
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.scale_factor_b
    :type: float

    Scale factor for vector B.

.. py:property:: normalize_vector_b
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.normalize_vector_b
    :type: bool

    Whether to normalize vector B.

.. py:property:: output_dimension_inheritance
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.output_dimension_inheritance
    :type: CRDN_DIMENSION_INHERITANCE

    Determines whether the output dimension is inherited or explicitly specified using OutputDimension.

.. py:property:: output_dimension
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.output_dimension
    :type: str

    A dimension to interpret the output vector.


