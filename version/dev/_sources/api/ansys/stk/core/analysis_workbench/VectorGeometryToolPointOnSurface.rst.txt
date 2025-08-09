VectorGeometryToolPointOnSurface
================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointOnSurface

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   The detic subpoint of the reference point as projected onto the central body.

.. py:currentmodule:: VectorGeometryToolPointOnSurface

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointOnSurface.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointOnSurface.reference_point`
              - Specify a reference point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointOnSurface.reference_shape`
              - Specify a reference shape.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointOnSurface.surface_type`
              - Specify a surface type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointOnSurface


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointOnSurface.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointOnSurface.reference_point
    :type: VectorGeometryToolPointReference

    Specify a reference point.

.. py:property:: reference_shape
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointOnSurface.reference_shape
    :type: SurfaceReferenceShapeType

    Specify a reference shape.

.. py:property:: surface_type
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointOnSurface.surface_type
    :type: SurfaceShapeType

    Specify a surface type.


