IVectorGeometryToolPlaneTriad
=============================

.. py:class:: IVectorGeometryToolPlaneTriad

   object
   
   A Plane containing points A, B and ReferencePont with the first axis aligned with the direction from the ReferencePoint to point A and the second axis toward the direction from the ReferencePoint to point B.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~point_a`
            * - :py:meth:`~point_b`
            * - :py:meth:`~reference_point`
            * - :py:meth:`~rotation_offset`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneTriad


Property detail
---------------

.. py:property:: point_a
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTriad.point_a
    :type: IAgCrdnPointRefTo

    Specify a point A.

.. py:property:: point_b
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTriad.point_b
    :type: IAgCrdnPointRefTo

    Specify a point B.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTriad.reference_point
    :type: IAgCrdnPointRefTo

    Specify a reference point.

.. py:property:: rotation_offset
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTriad.rotation_offset
    :type: float

    Specify an angle measured from X (Axis 1) away from Y (Axis 2).


