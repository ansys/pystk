VectorGeometryToolVectorCross
=============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorCross

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   The vector cross product of two vectors.

.. py:currentmodule:: VectorGeometryToolVectorCross

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorCross.from_vector`
              - Specify one of the two vectors which define the vector cross product.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorCross.to_vector`
              - Specify the second of the two vectors which define the vector cross product.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorCross.is_normalized`
              - Whether to convert the cross product of two vectors to a unit vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorCross.dimension`
              - Return a unit of measure, i.e. 'AngleUnit', 'DistanceUnit', etc.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorCross


Property detail
---------------

.. py:property:: from_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorCross.from_vector
    :type: VectorGeometryToolVectorReference

    Specify one of the two vectors which define the vector cross product.

.. py:property:: to_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorCross.to_vector
    :type: VectorGeometryToolVectorReference

    Specify the second of the two vectors which define the vector cross product.

.. py:property:: is_normalized
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorCross.is_normalized
    :type: bool

    Whether to convert the cross product of two vectors to a unit vector.

.. py:property:: dimension
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorCross.dimension
    :type: str

    Return a unit of measure, i.e. 'AngleUnit', 'DistanceUnit', etc.


