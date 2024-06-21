IVehicleGraphics3DBPlaneTargetPoint
===================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint

   object
   
   3D BPlane TargetPoint.

.. py:currentmodule:: IVehicleGraphics3DBPlaneTargetPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.set_position_type`
              - Set the position type of the BPlane target point.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.is_position_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.is_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.color`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.position_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.position_supported_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.position`


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
    :type: VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION

    Get the position type of the BPlane target point.

.. py:property:: position_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.position_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.position
    :type: IVehicleGraphics3DBPlaneTargetPointPosition

    Returns the BPlane target point position.


Method detail
-------------






.. py:method:: set_position_type(self, position: VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.set_position_type

    Set the position type of the BPlane target point.

    :Parameters:

    **position** : :obj:`~VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION`

    :Returns:

        :obj:`~None`

.. py:method:: is_position_type_supported(self, position: VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPoint.is_position_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **position** : :obj:`~VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION`

    :Returns:

        :obj:`~bool`



