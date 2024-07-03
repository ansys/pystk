IVectorGeometryToolVectorCross
==============================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorCross

   object
   
   The vector cross product of two vectors.

.. py:currentmodule:: IVectorGeometryToolVectorCross

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorCross.from_method`
              - Specify one of the two vectors which define the vector cross product.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorCross.to`
              - Specify the second of the two vectors which define the vector cross product.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorCross.is_normalized`
              - Whether to convert the cross product of two vectors to a unit vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorCross.dimension`
              - Returns a unit of measure, i.e. 'AngleUnit', 'DistanceUnit', etc.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorCross


Property detail
---------------

.. py:property:: from_method
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorCross.from_method
    :type: IVectorGeometryToolVectorRefTo

    Specify one of the two vectors which define the vector cross product.

.. py:property:: to
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorCross.to
    :type: IVectorGeometryToolVectorRefTo

    Specify the second of the two vectors which define the vector cross product.

.. py:property:: is_normalized
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorCross.is_normalized
    :type: bool

    Whether to convert the cross product of two vectors to a unit vector.

.. py:property:: dimension
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorCross.dimension
    :type: str

    Returns a unit of measure, i.e. 'AngleUnit', 'DistanceUnit', etc.


