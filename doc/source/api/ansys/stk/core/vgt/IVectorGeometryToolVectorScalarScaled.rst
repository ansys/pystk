IVectorGeometryToolVectorScalarScaled
=====================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled

   object
   
   Scaled version of the input vector using scalar.

.. py:currentmodule:: IVectorGeometryToolVectorScalarScaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.input_vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.input_scalar`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.scale_factor`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.normalize`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.dimension_inheritance`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.dimension`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorScalarScaled


Property detail
---------------

.. py:property:: input_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.input_vector
    :type: IVectorGeometryToolVector

    An input vector scaled by the scalar. Can be any VGT vector.

.. py:property:: input_scalar
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.input_scalar
    :type: ICalculationToolScalar

    A variable scale applied to the input vector. Can be based on any Scalar calculation.

.. py:property:: scale_factor
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.scale_factor
    :type: float

    A constant scale applied to the input vector.

.. py:property:: normalize
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.normalize
    :type: bool

    Whether to normalize the input vector before applying constant and variable scales.

.. py:property:: dimension_inheritance
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.dimension_inheritance
    :type: VECTOR_GEOMETRY_TOOL_VECTOR_SCALED_DIMENSION_INHERITANCE

    Whether or not to inherit dimension from the input vector or the scalar.

.. py:property:: dimension
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScalarScaled.dimension
    :type: str

    A dimension assigned to the output vector.


