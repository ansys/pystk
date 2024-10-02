VectorGeometryToolPlaneTrajectory
=================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPlaneTrajectory

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPlane`, :py:class:`~ansys.stk.core.vgt.IComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IComponent`

   The plane is defined on the basis of a trajectory of a Point with respect to a ReferenceSystem.

.. py:currentmodule:: VectorGeometryToolPlaneTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneTrajectory.point`
              - Specify a trajectory point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneTrajectory.reference_system`
              - Specify a reference system.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneTrajectory.rotation_offset`
              - Specify an angle measured from X (Axis 1) away from Y (Axis 2).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPlaneTrajectory


Property detail
---------------

.. py:property:: point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneTrajectory.point
    :type: VectorGeometryToolPointReference

    Specify a trajectory point.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneTrajectory.reference_system
    :type: VectorGeometryToolSystemReference

    Specify a reference system.

.. py:property:: rotation_offset
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneTrajectory.rotation_offset
    :type: float

    Specify an angle measured from X (Axis 1) away from Y (Axis 2).


