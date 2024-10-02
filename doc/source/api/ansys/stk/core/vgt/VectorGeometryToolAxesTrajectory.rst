VectorGeometryToolAxesTrajectory
================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAxesTrajectory

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.vgt.IComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Axes based on trajectory of the point relative to the reference coordinate system.

.. py:currentmodule:: VectorGeometryToolAxesTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesTrajectory.trajectory_point`
              - Specify a trajectory point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesTrajectory.reference_system`
              - Specify a reference system.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesTrajectory.trajectory_axes_type`
              - Specify a type of the trajectory's coordinate frame.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAxesTrajectory


Property detail
---------------

.. py:property:: trajectory_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesTrajectory.trajectory_point
    :type: VectorGeometryToolPointReference

    Specify a trajectory point.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesTrajectory.reference_system
    :type: VectorGeometryToolSystemReference

    Specify a reference system.

.. py:property:: trajectory_axes_type
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesTrajectory.trajectory_axes_type
    :type: TRAJECTORY_AXES_COORDINATES_TYPE

    Specify a type of the trajectory's coordinate frame.


