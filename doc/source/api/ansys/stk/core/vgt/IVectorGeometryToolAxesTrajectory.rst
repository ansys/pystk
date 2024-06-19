IVectorGeometryToolAxesTrajectory
=================================

.. py:class:: IVectorGeometryToolAxesTrajectory

   object
   
   Axes based on trajectory of the point relative to the reference coordinate system.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~trajectory_point`
            * - :py:meth:`~reference_system`
            * - :py:meth:`~trajectory_axes_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesTrajectory


Property detail
---------------

.. py:property:: trajectory_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTrajectory.trajectory_point
    :type: IAgCrdnPointRefTo

    Specify a trajectory point.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTrajectory.reference_system
    :type: IAgCrdnSystemRefTo

    Specify a reference system.

.. py:property:: trajectory_axes_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTrajectory.trajectory_axes_type
    :type: CRDN_TRAJECTORY_AXES_TYPE

    Specify a type of the trajectory's coordinate frame.


