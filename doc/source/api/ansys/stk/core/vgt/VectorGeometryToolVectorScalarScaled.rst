VectorGeometryToolVectorScalarScaled
====================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled

   Bases: :py:class:`~ansys.stk.core.vgt.IComponent`, :py:class:`~ansys.stk.core.vgt.IComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`

   Scaled version of the input vector using scalar.

.. py:currentmodule:: VectorGeometryToolVectorScalarScaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.input_vector`
              - An input vector scaled by the scalar. Can be any VGT vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.input_scalar`
              - A variable scale applied to the input vector. Can be based on any Scalar calculation.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.scale_factor`
              - A constant scale applied to the input vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.normalize`
              - Whether to normalize the input vector before applying constant and variable scales.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.dimension_inheritance`
              - Whether or not to inherit dimension from the input vector or the scalar.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.dimension`
              - A dimension assigned to the output vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorScalarScaled


Property detail
---------------

.. py:property:: input_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.input_vector
    :type: IVectorGeometryToolVector

    An input vector scaled by the scalar. Can be any VGT vector.

.. py:property:: input_scalar
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.input_scalar
    :type: ICalculationToolScalar

    A variable scale applied to the input vector. Can be based on any Scalar calculation.

.. py:property:: scale_factor
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.scale_factor
    :type: float

    A constant scale applied to the input vector.

.. py:property:: normalize
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.normalize
    :type: bool

    Whether to normalize the input vector before applying constant and variable scales.

.. py:property:: dimension_inheritance
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.dimension_inheritance
    :type: VECTOR_GEOMETRY_TOOL_SCALED_VECTOR_DIMENSION_INHERITANCE_OPTION_TYPE

    Whether or not to inherit dimension from the input vector or the scalar.

.. py:property:: dimension
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled.dimension
    :type: str

    A dimension assigned to the output vector.


