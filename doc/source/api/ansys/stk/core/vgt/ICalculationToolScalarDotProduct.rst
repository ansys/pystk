ICalculationToolScalarDotProduct
================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolScalarDotProduct

   object
   
   Dot product between two vectors.

.. py:currentmodule:: ICalculationToolScalarDotProduct

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDotProduct.vector_a`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDotProduct.normalize_vector_a`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDotProduct.vector_b`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDotProduct.normalize_vector_b`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDotProduct.dimension`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarDotProduct


Property detail
---------------

.. py:property:: vector_a
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDotProduct.vector_a
    :type: IVectorGeometryToolVector

    First vector.

.. py:property:: normalize_vector_a
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDotProduct.normalize_vector_a
    :type: bool

    Whether to normalize vector A.

.. py:property:: vector_b
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDotProduct.vector_b
    :type: IVectorGeometryToolVector

    Second vector.

.. py:property:: normalize_vector_b
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDotProduct.normalize_vector_b
    :type: bool

    Whether to normalize vector B.

.. py:property:: dimension
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDotProduct.dimension
    :type: str

    Returns a unit of measure, i.e. 'Angle', 'Distance', etc.


