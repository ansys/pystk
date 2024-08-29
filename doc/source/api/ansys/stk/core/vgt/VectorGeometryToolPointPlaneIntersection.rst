VectorGeometryToolPointPlaneIntersection
========================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPointPlaneIntersection

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Point on a plane located along a given direction looking from a given origin.

.. py:currentmodule:: VectorGeometryToolPointPlaneIntersection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointPlaneIntersection.direction_vector`
              - Specify a direction vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointPlaneIntersection.reference_plane`
              - Specify a reference plane.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointPlaneIntersection.origin_point`
              - Specify the origin point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPointPlaneIntersection


Property detail
---------------

.. py:property:: direction_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointPlaneIntersection.direction_vector
    :type: VectorGeometryToolVectorRefTo

    Specify a direction vector.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointPlaneIntersection.reference_plane
    :type: VectorGeometryToolPlaneRefTo

    Specify a reference plane.

.. py:property:: origin_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointPlaneIntersection.origin_point
    :type: VectorGeometryToolPointRefTo

    Specify the origin point.


