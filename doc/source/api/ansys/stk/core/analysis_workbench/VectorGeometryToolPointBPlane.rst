VectorGeometryToolPointBPlane
=============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointBPlane

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   B-Plane point using the selected target body.

.. py:currentmodule:: VectorGeometryToolPointBPlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointBPlane.direction`
              - Specify a direction (incoming or outgoing).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointBPlane.point_type`
              - Specify a point type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointBPlane.target_body`
              - Specify a target central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointBPlane.trajectory`
              - Specify a trajectory point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointBPlane


Property detail
---------------

.. py:property:: direction
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointBPlane.direction
    :type: AsymptoteDirectionType

    Specify a direction (incoming or outgoing).

.. py:property:: point_type
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointBPlane.point_type
    :type: PointBPlaneType

    Specify a point type.

.. py:property:: target_body
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointBPlane.target_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a target central body.

.. py:property:: trajectory
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointBPlane.trajectory
    :type: VectorGeometryToolPointReference

    Specify a trajectory point.


