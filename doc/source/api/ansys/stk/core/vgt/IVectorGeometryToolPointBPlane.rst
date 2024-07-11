IVectorGeometryToolPointBPlane
==============================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPointBPlane

   object
   
   B-Plane point using the selected target body.

.. py:currentmodule:: IVectorGeometryToolPointBPlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointBPlane.target_body`
              - Specify a target central body.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointBPlane.trajectory`
              - Specify a trajectory point.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointBPlane.point_type`
              - Specify a point type.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointBPlane.direction`
              - Specify a direction (incoming or outgoing).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointBPlane


Property detail
---------------

.. py:property:: target_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointBPlane.target_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a target central body.

.. py:property:: trajectory
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointBPlane.trajectory
    :type: IVectorGeometryToolPointRefTo

    Specify a trajectory point.

.. py:property:: point_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointBPlane.point_type
    :type: VECTOR_GEOMETRY_TOOL_POINT_B_PLANE_TYPE

    Specify a point type.

.. py:property:: direction
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointBPlane.direction
    :type: CRDN_DIRECTION_TYPE

    Specify a direction (incoming or outgoing).


