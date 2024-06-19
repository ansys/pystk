IVectorGeometryToolPlaneTrajectory
==================================

.. py:class:: IVectorGeometryToolPlaneTrajectory

   object
   
   The plane is defined on the basis of a trajectory of a Point with respect to a ReferenceSystem.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~point`
            * - :py:meth:`~reference_system`
            * - :py:meth:`~rotation_offset`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneTrajectory


Property detail
---------------

.. py:property:: point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTrajectory.point
    :type: IAgCrdnPointRefTo

    Specify a trajectory point.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTrajectory.reference_system
    :type: IAgCrdnSystemRefTo

    Specify a reference system.

.. py:property:: rotation_offset
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneTrajectory.rotation_offset
    :type: float

    Specify an angle measured from X (Axis 1) away from Y (Axis 2).


