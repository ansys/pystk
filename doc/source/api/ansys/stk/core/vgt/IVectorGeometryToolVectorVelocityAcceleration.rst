IVectorGeometryToolVectorVelocityAcceleration
=============================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorVelocityAcceleration

   object
   
   Velocity vector of a point in a coordinate system.

.. py:currentmodule:: IVectorGeometryToolVectorVelocityAcceleration

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorVelocityAcceleration.reference_system`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorVelocityAcceleration.point`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorVelocityAcceleration.differencing_time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorVelocityAcceleration


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorVelocityAcceleration.reference_system
    :type: IVectorGeometryToolSystem

    A reference (coordinate) system. Can be any VGT system.

.. py:property:: point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorVelocityAcceleration.point
    :type: IVectorGeometryToolPoint

    A point which velocity this vector represents. Can be any VGT point.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorVelocityAcceleration.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.


