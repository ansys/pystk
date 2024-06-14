IVectorGeometryToolVectorCross
==============================

.. py:class:: IVectorGeometryToolVectorCross

   object
   
   The vector cross product of two vectors.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~from_method`
            * - :py:meth:`~to`
            * - :py:meth:`~is_normalized`
            * - :py:meth:`~dimension`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorCross


Property detail
---------------

.. py:property:: from_method
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorCross.from_method
    :type: "IAgCrdnVectorRefTo"

    Specify one of the two vectors which define the vector cross product.

.. py:property:: to
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorCross.to
    :type: "IAgCrdnVectorRefTo"

    Specify the second of the two vectors which define the vector cross product.

.. py:property:: is_normalized
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorCross.is_normalized
    :type: bool

    Whether to convert the cross product of two vectors to a unit vector.

.. py:property:: dimension
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorCross.dimension
    :type: str

    Returns a unit of measure, i.e. 'AngleUnit', 'DistanceUnit', etc.


