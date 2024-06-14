IVehicleGraphics3DBPlaneTargetPoint
===================================

.. py:class:: IVehicleGraphics3DBPlaneTargetPoint

   object
   
   3D BPlane TargetPoint.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_position_type`
              - Set the position type of the BPlane target point.
            * - :py:meth:`~is_position_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~color`
            * - :py:meth:`~position_type`
            * - :py:meth:`~position_supported_types`
            * - :py:meth:`~position`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DBPlaneTargetPoint


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.is_visible
    :type: bool

    Whether the Target Point is displayed.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.color
    :type: agcolor.Color

    Gets or sets the color of the Target Point.

.. py:property:: position_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.position_type
    :type: "VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION"

    Get the position type of the BPlane target point.

.. py:property:: position_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.position_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.position
    :type: "IAgVeVOBPlaneTargetPointPosition"

    Returns the BPlane target point position.


Method detail
-------------






.. py:method:: set_position_type(self, position:"VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION") -> None

    Set the position type of the BPlane target point.

    :Parameters:

    **position** : :obj:`~"VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION"`

    :Returns:

        :obj:`~None`

.. py:method:: is_position_type_supported(self, position:"VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **position** : :obj:`~"VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION"`

    :Returns:

        :obj:`~bool`



