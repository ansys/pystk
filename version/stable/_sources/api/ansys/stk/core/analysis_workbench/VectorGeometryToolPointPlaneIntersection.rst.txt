VectorGeometryToolPointPlaneIntersection
========================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Point on a plane located along a given direction looking from a given origin.

.. py:currentmodule:: VectorGeometryToolPointPlaneIntersection

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.direction_vector`
              - Specify a direction vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.reference_plane`
              - Specify a reference plane.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.origin_point`
              - Specify the origin point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointPlaneIntersection


Property detail
---------------

.. py:property:: direction_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.direction_vector
    :type: VectorGeometryToolVectorReference

    Specify a direction vector.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.reference_plane
    :type: VectorGeometryToolPlaneReference

    Specify a reference plane.

.. py:property:: origin_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.origin_point
    :type: VectorGeometryToolPointReference

    Specify the origin point.


