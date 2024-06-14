ICalculationToolScalarDotProduct
================================

.. py:class:: ICalculationToolScalarDotProduct

   object
   
   Dot product between two vectors.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~vector_a`
            * - :py:meth:`~normalize_vector_a`
            * - :py:meth:`~vector_b`
            * - :py:meth:`~normalize_vector_b`
            * - :py:meth:`~dimension`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarDotProduct


Property detail
---------------

.. py:property:: vector_a
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDotProduct.vector_a
    :type: "IAgCrdnVector"

    First vector.

.. py:property:: normalize_vector_a
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDotProduct.normalize_vector_a
    :type: bool

    Whether to normalize vector A.

.. py:property:: vector_b
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDotProduct.vector_b
    :type: "IAgCrdnVector"

    Second vector.

.. py:property:: normalize_vector_b
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDotProduct.normalize_vector_b
    :type: bool

    Whether to normalize vector B.

.. py:property:: dimension
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDotProduct.dimension
    :type: str

    Returns a unit of measure, i.e. 'Angle', 'Distance', etc.


