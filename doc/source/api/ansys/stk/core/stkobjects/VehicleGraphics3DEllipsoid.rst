VehicleGraphics3DEllipsoid
==========================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DProximityAreaObject`

   Define an ellipsoid around the vehicle object.

.. py:currentmodule:: VehicleGraphics3DEllipsoid

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.x_semiaxis_length`
              - Indicate how far along the X axis of the reference frame the box extends. Value must be greater than 0.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.y_semiaxis_length`
              - Indicate how far along the Y axis of the reference frame the box extends. Value must be greater than 0.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.z_semiaxis_length`
              - Indicate how far along the Z axis of the reference frame the box extends. Value must be greater than 0.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.x_axis_offset`
              - Get or set the distance to offset the box (positive or negative) along the X axis of the reference frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.y_axis_offset`
              - Get or set the distance to offset the box (positive or negative) along the Y axis of the reference frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.z_axis_offset`
              - Get or set the distance to offset the box (positive or negative) along the Z axis of the reference frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.use_translucency`
              - Specify a translucency of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.translucency`
              - Get or set the translucency of the object. Valid values are 0 - 100, where 0 is opaque and 100 is transparent.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.granularity`
              - Indicate the number of points used to draw the ellipsoid. Lower numbers create a better ellipsoid and higher numbers make the ellipsoid draw faster.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.reference_frame`
              - Get or set the reference axes that is used to align the ellipsoid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DEllipsoid


Property detail
---------------

.. py:property:: x_semiaxis_length
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.x_semiaxis_length
    :type: float

    Indicate how far along the X axis of the reference frame the box extends. Value must be greater than 0.

.. py:property:: y_semiaxis_length
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.y_semiaxis_length
    :type: float

    Indicate how far along the Y axis of the reference frame the box extends. Value must be greater than 0.

.. py:property:: z_semiaxis_length
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.z_semiaxis_length
    :type: float

    Indicate how far along the Z axis of the reference frame the box extends. Value must be greater than 0.

.. py:property:: x_axis_offset
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.x_axis_offset
    :type: float

    Get or set the distance to offset the box (positive or negative) along the X axis of the reference frame.

.. py:property:: y_axis_offset
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.y_axis_offset
    :type: float

    Get or set the distance to offset the box (positive or negative) along the Y axis of the reference frame.

.. py:property:: z_axis_offset
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.z_axis_offset
    :type: float

    Get or set the distance to offset the box (positive or negative) along the Z axis of the reference frame.

.. py:property:: use_translucency
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.use_translucency
    :type: bool

    Specify a translucency of the object.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.translucency
    :type: float

    Get or set the translucency of the object. Valid values are 0 - 100, where 0 is opaque and 100 is transparent.

.. py:property:: granularity
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.granularity
    :type: float

    Indicate the number of points used to draw the ellipsoid. Lower numbers create a better ellipsoid and higher numbers make the ellipsoid draw faster.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid.reference_frame
    :type: IVectorGeometryToolAxes

    Get or set the reference axes that is used to align the ellipsoid.


