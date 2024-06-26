IVectorGeometryToolPlaneTrajectory
==================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPlaneTrajectory

   object
   
   The plane is defined on the basis of a trajectory of a Point with respect to a ReferenceSystem.

.. py:currentmodule:: IVectorGeometryToolPlaneTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneTrajectory.point`
              - Specify a trajectory point.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneTrajectory.reference_system`
              - Specify a reference system.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneTrajectory.rotation_offset`
              - Specify an angle measured from X (Axis 1) away from Y (Axis 2).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneTrajectory


Property detail
---------------

.. py:property:: point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTrajectory.point
    :type: IVectorGeometryToolPointRefTo

    Specify a trajectory point.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTrajectory.reference_system
    :type: IVectorGeometryToolSystemRefTo

    Specify a reference system.

.. py:property:: rotation_offset
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTrajectory.rotation_offset
    :type: float

    Specify an angle measured from X (Axis 1) away from Y (Axis 2).


