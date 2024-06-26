IVehicleGraphics3DControlBox
============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox

   IVehicleGraphics3DProximityAreaObject
   
   Define a volume around the object that moves with the object.

.. py:currentmodule:: IVehicleGraphics3DControlBox

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.use_translucency`
              - Specifies a translucency of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.translucency`
              - Gets or sets the translucency of the object. Valid values are 0 - 100, where 0 is opaque and 100 is transparent. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.reference_frame`
              - Gets or sets the reference axes that is used to align the ellipsoid.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.x_axis_length`
              - Indicates how far along the velocity vector the box extends. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.y_axis_length`
              - Indicates how far along the orbit normal the box extends. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.z_axis_length`
              - Indicates how far along the orbit plane the box extends. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.x_offset`
              - Gets or sets the distance to offset the box (forward or backward) along the velocity vector. A positive value moves the box forward along the velocity vector. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.y_offset`
              - Gets or sets the distance to offset the box (left or right) along the velocity vector. A positive value moves the box right along the vector 90 degrees clockwise from the velocity vector. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.z_offset`
              - Gets or sets the distance to offset the box (up or down). A positive value moves the box down, towards the ground. Uses Distance Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DControlBox


Property detail
---------------

.. py:property:: use_translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.use_translucency
    :type: bool

    Specifies a translucency of the object.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.translucency
    :type: float

    Gets or sets the translucency of the object. Valid values are 0 - 100, where 0 is opaque and 100 is transparent. Dimensionless.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.reference_frame
    :type: IVectorGeometryToolAxes

    Gets or sets the reference axes that is used to align the ellipsoid.

.. py:property:: x_axis_length
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.x_axis_length
    :type: float

    Indicates how far along the velocity vector the box extends. Uses Distance Dimension.

.. py:property:: y_axis_length
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.y_axis_length
    :type: float

    Indicates how far along the orbit normal the box extends. Uses Distance Dimension.

.. py:property:: z_axis_length
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.z_axis_length
    :type: float

    Indicates how far along the orbit plane the box extends. Uses Distance Dimension.

.. py:property:: x_offset
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.x_offset
    :type: float

    Gets or sets the distance to offset the box (forward or backward) along the velocity vector. A positive value moves the box forward along the velocity vector. Uses Distance Dimension.

.. py:property:: y_offset
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.y_offset
    :type: float

    Gets or sets the distance to offset the box (left or right) along the velocity vector. A positive value moves the box right along the vector 90 degrees clockwise from the velocity vector. Uses Distance Dimension.

.. py:property:: z_offset
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DControlBox.z_offset
    :type: float

    Gets or sets the distance to offset the box (up or down). A positive value moves the box down, towards the ground. Uses Distance Dimension.


