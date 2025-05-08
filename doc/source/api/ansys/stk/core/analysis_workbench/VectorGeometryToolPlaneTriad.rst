VectorGeometryToolPlaneTriad
============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTriad

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A Plane containing points PointA, PointB and ReferencePont with the first axis aligned with the direction from the ReferencePoint to PointA and the second axis toward the direction from the ReferencePoint to PointB.

.. py:currentmodule:: VectorGeometryToolPlaneTriad

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTriad.point_a`
              - Specify a point A.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTriad.point_b`
              - Specify a point B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTriad.reference_point`
              - Specify a reference point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTriad.rotation_offset`
              - Specify an angle measured from X (Axis 1) away from Y (Axis 2).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPlaneTriad


Property detail
---------------

.. py:property:: point_a
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTriad.point_a
    :type: VectorGeometryToolPointReference

    Specify a point A.

.. py:property:: point_b
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTriad.point_b
    :type: VectorGeometryToolPointReference

    Specify a point B.

.. py:property:: reference_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTriad.reference_point
    :type: VectorGeometryToolPointReference

    Specify a reference point.

.. py:property:: rotation_offset
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTriad.rotation_offset
    :type: float

    Specify an angle measured from X (Axis 1) away from Y (Axis 2).


