VectorGeometryToolPointBPlane
=============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPointBPlane

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   B-Plane point using the selected target body.

.. py:currentmodule:: VectorGeometryToolPointBPlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointBPlane.target_body`
              - Specify a target central body.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointBPlane.trajectory`
              - Specify a trajectory point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointBPlane.point_type`
              - Specify a point type.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointBPlane.direction`
              - Specify a direction (incoming or outgoing).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPointBPlane


Property detail
---------------

.. py:property:: target_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointBPlane.target_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a target central body.

.. py:property:: trajectory
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointBPlane.trajectory
    :type: VectorGeometryToolPointReference

    Specify a trajectory point.

.. py:property:: point_type
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointBPlane.point_type
    :type: PointBPlaneType

    Specify a point type.

.. py:property:: direction
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointBPlane.direction
    :type: AsymptoteDirectionType

    Specify a direction (incoming or outgoing).


