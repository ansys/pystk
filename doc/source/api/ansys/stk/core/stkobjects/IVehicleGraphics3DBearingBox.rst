IVehicleGraphics3DBearingBox
============================

.. py:class:: IVehicleGraphics3DBearingBox

   IVehicleGraphics3DProximityAreaObject
   
   Define a volume, relative to a bearing from the North, around an object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~bearing`
            * - :py:meth:`~length`
            * - :py:meth:`~width`
            * - :py:meth:`~height`
            * - :py:meth:`~length_offset`
            * - :py:meth:`~width_offset`
            * - :py:meth:`~height_offset`
            * - :py:meth:`~use_translucency`
            * - :py:meth:`~translucency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DBearingBox


Property detail
---------------

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingBox.bearing
    :type: float

    Gets or sets the bearing value, relative to North. Uses Angle Dimension.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingBox.length
    :type: float

    Indicates the length of the box, along the bearing. The value must be greater than 0. Uses Distance Dimension.

.. py:property:: width
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingBox.width
    :type: float

    Indicates the width of the box, across the bearing. The value must be greater than 0. Uses Distance Dimension.

.. py:property:: height
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingBox.height
    :type: float

    Indicates the Height of the box. Uses Distance Dimension.

.. py:property:: length_offset
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingBox.length_offset
    :type: float

    Gets or sets the distance to offset the box (forward or backward) along the bearing. A positive LengthOffset value moves the box forward. Uses Distance Dimension.

.. py:property:: width_offset
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingBox.width_offset
    :type: float

    Gets or sets the distance to offset the box (left or right) along the bearing. A positive value moves the box to the right. Uses Distance Dimension.

.. py:property:: height_offset
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingBox.height_offset
    :type: float

    Gets or sets the distance to offset the box (up or down). A positive value moves the box down, towards the ground. Uses Distance Dimension.

.. py:property:: use_translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingBox.use_translucency
    :type: bool

    Specifies a translucency of the object.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingBox.translucency
    :type: float

    Gets or sets the translucency of the object. Valid values are 0 - 100, where 0 is opaque and 100 is transparent. Dimensionless.


