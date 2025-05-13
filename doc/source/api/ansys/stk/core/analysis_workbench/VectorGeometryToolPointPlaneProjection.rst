VectorGeometryToolPointPlaneProjection
======================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneProjection

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   The projection of a point onto a reference plane. Specify the Source Point and Reference Plane.

.. py:currentmodule:: VectorGeometryToolPointPlaneProjection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneProjection.source_point`
              - Specify a source point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneProjection.reference_plane`
              - Specify a reference plane.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointPlaneProjection


Property detail
---------------

.. py:property:: source_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneProjection.source_point
    :type: VectorGeometryToolPointReference

    Specify a source point.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneProjection.reference_plane
    :type: VectorGeometryToolPlaneReference

    Specify a reference plane.


