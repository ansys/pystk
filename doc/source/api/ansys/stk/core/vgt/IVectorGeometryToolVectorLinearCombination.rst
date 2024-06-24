IVectorGeometryToolVectorLinearCombination
==========================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination

   object
   
   Linear combination of two input vectors.

.. py:currentmodule:: IVectorGeometryToolVectorLinearCombination

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.vector_a`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.scale_factor_a`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.normalize_vector_a`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.vector_b`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.scale_factor_b`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.normalize_vector_b`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.output_dimension_inheritance`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.output_dimension`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorLinearCombination


Property detail
---------------

.. py:property:: vector_a
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.vector_a
    :type: IVectorGeometryToolVector

    Vector A can be any VGT vector.

.. py:property:: scale_factor_a
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.scale_factor_a
    :type: float

    Scale factor for vector A.

.. py:property:: normalize_vector_a
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.normalize_vector_a
    :type: bool

    Whether to normalize vector A.

.. py:property:: vector_b
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.vector_b
    :type: IVectorGeometryToolVector

    Vector B can be any VGT vector.

.. py:property:: scale_factor_b
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.scale_factor_b
    :type: float

    Scale factor for vector B.

.. py:property:: normalize_vector_b
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.normalize_vector_b
    :type: bool

    Whether to normalize vector B.

.. py:property:: output_dimension_inheritance
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.output_dimension_inheritance
    :type: CRDN_DIMENSION_INHERITANCE

    Determines whether the output dimension is inherited or explicitly specified using OutputDimension.

.. py:property:: output_dimension
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorLinearCombination.output_dimension
    :type: str

    A dimension to interpret the output vector.


