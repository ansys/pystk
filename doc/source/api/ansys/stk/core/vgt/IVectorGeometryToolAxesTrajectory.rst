IVectorGeometryToolAxesTrajectory
=================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesTrajectory

   object
   
   Axes based on trajectory of the point relative to the reference coordinate system.

.. py:currentmodule:: IVectorGeometryToolAxesTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesTrajectory.trajectory_point`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesTrajectory.reference_system`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesTrajectory.trajectory_axes_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesTrajectory


Property detail
---------------

.. py:property:: trajectory_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTrajectory.trajectory_point
    :type: IVectorGeometryToolPointRefTo

    Specify a trajectory point.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTrajectory.reference_system
    :type: IVectorGeometryToolSystemRefTo

    Specify a reference system.

.. py:property:: trajectory_axes_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTrajectory.trajectory_axes_type
    :type: CRDN_TRAJECTORY_AXES_TYPE

    Specify a type of the trajectory's coordinate frame.


