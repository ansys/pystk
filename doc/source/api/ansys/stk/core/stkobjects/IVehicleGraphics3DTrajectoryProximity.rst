IVehicleGraphics3DTrajectoryProximity
=====================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity

   IVehicleGraphics3DProximity
   
   Proximity graphics for a launch vehicle or missile.

.. py:currentmodule:: IVehicleGraphics3DTrajectoryProximity

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.control_box`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.bearing_box`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.bearing_ellipse`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.line_of_bearing`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.aou_label_swap_distance`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.ellipsoid`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DTrajectoryProximity


Property detail
---------------

.. py:property:: control_box
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.control_box
    :type: IVehicleGraphics3DControlBox

    Get the control box parameters.

.. py:property:: bearing_box
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.bearing_box
    :type: IVehicleGraphics3DBearingBox

    Get the bearing box parameters.

.. py:property:: bearing_ellipse
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.bearing_ellipse
    :type: IVehicleGraphics3DBearingEllipse

    Get the bearing ellipse parameters.

.. py:property:: line_of_bearing
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.line_of_bearing
    :type: IVehicleGraphics3DLineOfBearing

    Get the line of bearing parameters.

.. py:property:: aou_label_swap_distance
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.aou_label_swap_distance
    :type: IGraphics3DLabelSwapDistance

    Area of uncertainty label swap distance.

.. py:property:: ellipsoid
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.ellipsoid
    :type: IVehicleGraphics3DEllipsoid

    Defines the ellipsoid parameters.


