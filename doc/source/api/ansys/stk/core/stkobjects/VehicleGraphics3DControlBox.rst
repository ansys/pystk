VehicleGraphics3DControlBox
===========================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DControlBox

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DProximityAreaObject`

   Define a volume around the object that moves with the object.

.. py:currentmodule:: VehicleGraphics3DControlBox

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.use_translucency`
              - Specify a translucency of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.translucency`
              - Get or set the translucency of the object. Valid values are 0 - 100, where 0 is opaque and 100 is transparent. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.reference_frame`
              - Get or set the reference axes that is used to align the ellipsoid.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.x_axis_length`
              - Indicate how far along the velocity vector the box extends. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.y_axis_length`
              - Indicate how far along the orbit normal the box extends. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.z_axis_length`
              - Indicate how far along the orbit plane the box extends. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.x_offset`
              - Get or set the distance to offset the box (forward or backward) along the velocity vector. A positive value moves the box forward along the velocity vector. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.y_offset`
              - Get or set the distance to offset the box (left or right) along the velocity vector. A positive value moves the box right along the vector 90 degrees clockwise from the velocity vector. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.z_offset`
              - Get or set the distance to offset the box (up or down). A positive value moves the box down, towards the ground. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DControlBox


Property detail
---------------

.. py:property:: use_translucency
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.use_translucency
    :type: bool

    Specify a translucency of the object.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.translucency
    :type: float

    Get or set the translucency of the object. Valid values are 0 - 100, where 0 is opaque and 100 is transparent. Dimensionless.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.reference_frame
    :type: IVectorGeometryToolAxes

    Get or set the reference axes that is used to align the ellipsoid.

.. py:property:: x_axis_length
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.x_axis_length
    :type: float

    Indicate how far along the velocity vector the box extends. Uses Distance Dimension.

.. py:property:: y_axis_length
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.y_axis_length
    :type: float

    Indicate how far along the orbit normal the box extends. Uses Distance Dimension.

.. py:property:: z_axis_length
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.z_axis_length
    :type: float

    Indicate how far along the orbit plane the box extends. Uses Distance Dimension.

.. py:property:: x_offset
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.x_offset
    :type: float

    Get or set the distance to offset the box (forward or backward) along the velocity vector. A positive value moves the box forward along the velocity vector. Uses Distance Dimension.

.. py:property:: y_offset
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.y_offset
    :type: float

    Get or set the distance to offset the box (left or right) along the velocity vector. A positive value moves the box right along the vector 90 degrees clockwise from the velocity vector. Uses Distance Dimension.

.. py:property:: z_offset
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DControlBox.z_offset
    :type: float

    Get or set the distance to offset the box (up or down). A positive value moves the box down, towards the ground. Uses Distance Dimension.


