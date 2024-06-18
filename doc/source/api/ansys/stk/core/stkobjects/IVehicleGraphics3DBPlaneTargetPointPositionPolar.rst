IVehicleGraphics3DBPlaneTargetPointPositionPolar
================================================

.. py:class:: IVehicleGraphics3DBPlaneTargetPointPositionPolar

   IVehicleGraphics3DBPlaneTargetPointPosition
   
   3D BPlane target point position polar.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~b_magnitude`
            * - :py:meth:`~theta`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DBPlaneTargetPointPositionPolar


Property detail
---------------

.. py:property:: b_magnitude
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPointPositionPolar.b_magnitude
    :type: float

    Gets or sets the magnitude of B vector. For more information see \"B-Plane Targeting\". Uses Distance Dimension.

.. py:property:: theta
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPointPositionPolar.theta
    :type: float

    Gets or sets the angle of B vector measured in the B-plane from T vector toward R vector. Uses Angle Dimension.


