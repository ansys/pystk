VectorGeometryToolPointPlaneProjection
======================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPointPlaneProjection

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   The projection of a point onto a reference plane. Specify the Source Point and Reference Plane.

.. py:currentmodule:: VectorGeometryToolPointPlaneProjection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointPlaneProjection.source_point`
              - Specify a source point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointPlaneProjection.reference_plane`
              - Specify a reference plane.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPointPlaneProjection


Property detail
---------------

.. py:property:: source_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointPlaneProjection.source_point
    :type: VectorGeometryToolPointRefTo

    Specify a source point.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointPlaneProjection.reference_plane
    :type: VectorGeometryToolPlaneRefTo

    Specify a reference plane.


