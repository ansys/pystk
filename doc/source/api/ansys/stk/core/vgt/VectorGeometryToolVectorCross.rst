VectorGeometryToolVectorCross
=============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorCross

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   The vector cross product of two vectors.

.. py:currentmodule:: VectorGeometryToolVectorCross

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorCross.from_method`
              - Specify one of the two vectors which define the vector cross product.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorCross.to`
              - Specify the second of the two vectors which define the vector cross product.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorCross.is_normalized`
              - Whether to convert the cross product of two vectors to a unit vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorCross.dimension`
              - Returns a unit of measure, i.e. 'AngleUnit', 'DistanceUnit', etc.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorCross


Property detail
---------------

.. py:property:: from_method
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorCross.from_method
    :type: VectorGeometryToolVectorRefTo

    Specify one of the two vectors which define the vector cross product.

.. py:property:: to
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorCross.to
    :type: VectorGeometryToolVectorRefTo

    Specify the second of the two vectors which define the vector cross product.

.. py:property:: is_normalized
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorCross.is_normalized
    :type: bool

    Whether to convert the cross product of two vectors to a unit vector.

.. py:property:: dimension
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorCross.dimension
    :type: str

    Returns a unit of measure, i.e. 'AngleUnit', 'DistanceUnit', etc.


