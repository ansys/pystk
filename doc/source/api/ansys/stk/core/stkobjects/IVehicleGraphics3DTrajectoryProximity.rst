IVehicleGraphics3DTrajectoryProximity
=====================================

.. py:class:: IVehicleGraphics3DTrajectoryProximity

   IVehicleGraphics3DProximity
   
   Proximity graphics for a launch vehicle or missile.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~control_box`
            * - :py:meth:`~bearing_box`
            * - :py:meth:`~bearing_ellipse`
            * - :py:meth:`~line_of_bearing`
            * - :py:meth:`~aou_label_swap_distance`
            * - :py:meth:`~ellipsoid`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DTrajectoryProximity


Property detail
---------------

.. py:property:: control_box
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.control_box
    :type: "IAgVeVOControlBox"

    Get the control box parameters.

.. py:property:: bearing_box
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.bearing_box
    :type: "IAgVeVOBearingBox"

    Get the bearing box parameters.

.. py:property:: bearing_ellipse
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.bearing_ellipse
    :type: "IAgVeVOBearingEllipse"

    Get the bearing ellipse parameters.

.. py:property:: line_of_bearing
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.line_of_bearing
    :type: "IAgVeVOLineOfBearing"

    Get the line of bearing parameters.

.. py:property:: aou_label_swap_distance
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.aou_label_swap_distance
    :type: "IAgVOLabelSwapDistance"

    Area of uncertainty label swap distance.

.. py:property:: ellipsoid
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryProximity.ellipsoid
    :type: "IAgVeVOEllipsoid"

    Defines the ellipsoid parameters.


