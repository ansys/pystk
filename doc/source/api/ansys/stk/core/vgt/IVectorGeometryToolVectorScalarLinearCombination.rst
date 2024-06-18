IVectorGeometryToolVectorScalarLinearCombination
================================================

.. py:class:: IVectorGeometryToolVectorScalarLinearCombination

   object
   
   Linear combination of two input vectors using scalars.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~vector_a`
            * - :py:meth:`~scale_factor_a`
            * - :py:meth:`~normalize_vector_a`
            * - :py:meth:`~use_scale_from_scalar_a`
            * - :py:meth:`~use_scale_from_scalar_b`
            * - :py:meth:`~scalar_a`
            * - :py:meth:`~scalar_b`
            * - :py:meth:`~vector_b`
            * - :py:meth:`~scale_factor_b`
            * - :py:meth:`~normalize_vector_b`
            * - :py:meth:`~output_dimension_inheritance`
            * - :py:meth:`~output_dimension`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorScalarLinearCombination


Property detail
---------------

.. py:property:: vector_a
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.vector_a
    :type: "IAgCrdnVector"

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
    :type: "IAgCrdnCalcScalar"

    Scalar scale A. Can be any Scalar calculation.

.. py:property:: scalar_b
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.scalar_b
    :type: "IAgCrdnCalcScalar"

    Scalar scale B. Can be any Scalar calculation.

.. py:property:: vector_b
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.vector_b
    :type: "IAgCrdnVector"

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
    :type: "CRDN_DIMENSION_INHERITANCE"

    Determines whether the output dimension is inherited or explicitly specified using OutputDimension.

.. py:property:: output_dimension
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarLinearCombination.output_dimension
    :type: str

    A dimension to interpret the output vector.


