IVehicleGraphics3DEllipsoid
===========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid

   IVehicleGraphics3DProximityAreaObject
   
   Define an ellipsoid around the vehicle object.

.. py:currentmodule:: IVehicleGraphics3DEllipsoid

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.x_semi_axis_length`
              - Indicates how far along the X axis of the reference frame the box extends. Value must be greater than 0.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.y_semi_axis_length`
              - Indicates how far along the Y axis of the reference frame the box extends. Value must be greater than 0.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.z_semi_axis_length`
              - Indicates how far along the Z axis of the reference frame the box extends. Value must be greater than 0.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.x_axis_offset`
              - Gets or sets the distance to offset the box (positive or negative) along the X axis of the reference frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.y_axis_offset`
              - Gets or sets the distance to offset the box (positive or negative) along the Y axis of the reference frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.z_axis_offset`
              - Gets or sets the distance to offset the box (positive or negative) along the Z axis of the reference frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.use_translucency`
              - Specifies a translucency of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.translucency`
              - Gets or sets the translucency of the object. Valid values are 0 - 100, where 0 is opaque and 100 is transparent.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.granularity`
              - Indicates the number of points used to draw the ellipsoid. Lower numbers create a better ellipsoid and higher numbers make the ellipsoid draw faster.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.reference_frame`
              - Gets or sets the reference axes that is used to align the ellipsoid.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DEllipsoid


Property detail
---------------

.. py:property:: x_semi_axis_length
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.x_semi_axis_length
    :type: float

    Indicates how far along the X axis of the reference frame the box extends. Value must be greater than 0.

.. py:property:: y_semi_axis_length
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.y_semi_axis_length
    :type: float

    Indicates how far along the Y axis of the reference frame the box extends. Value must be greater than 0.

.. py:property:: z_semi_axis_length
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.z_semi_axis_length
    :type: float

    Indicates how far along the Z axis of the reference frame the box extends. Value must be greater than 0.

.. py:property:: x_axis_offset
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.x_axis_offset
    :type: float

    Gets or sets the distance to offset the box (positive or negative) along the X axis of the reference frame.

.. py:property:: y_axis_offset
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.y_axis_offset
    :type: float

    Gets or sets the distance to offset the box (positive or negative) along the Y axis of the reference frame.

.. py:property:: z_axis_offset
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.z_axis_offset
    :type: float

    Gets or sets the distance to offset the box (positive or negative) along the Z axis of the reference frame.

.. py:property:: use_translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.use_translucency
    :type: bool

    Specifies a translucency of the object.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.translucency
    :type: float

    Gets or sets the translucency of the object. Valid values are 0 - 100, where 0 is opaque and 100 is transparent.

.. py:property:: granularity
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.granularity
    :type: float

    Indicates the number of points used to draw the ellipsoid. Lower numbers create a better ellipsoid and higher numbers make the ellipsoid draw faster.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DEllipsoid.reference_frame
    :type: IVectorGeometryToolAxes

    Gets or sets the reference axes that is used to align the ellipsoid.


