VehicleGraphics3DBearingEllipse
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DProximityAreaObject`

   Define an ellipse, relative to a bearing from the North, around the object.

.. py:currentmodule:: VehicleGraphics3DBearingEllipse

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.bearing`
              - Gets or sets the bearing value, relative to North. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.semi_major_axis`
              - Defines the major axis for the ellipse. The value must be greater than 0. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.semi_minor_axis`
              - Defines the minor axis for the ellipse. The value must be greater than 0. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.granularity`
              - Indicates the number of points used to draw the ellipse. Lower numbers create a better ellipse and higher numbers make the ellipse draw faster. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.major_axis_offset`
              - Gets or sets the distance to offset the box (forward or backward) along the bearing. A positive MajorAxisOffset value moves the box forward. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.minor_axis_offset`
              - Gets or sets the distance to offset the box (left or right) along the bearing. A positive MinorAxisOffset value moves the box to the right. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DBearingEllipse


Property detail
---------------

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.bearing
    :type: float

    Gets or sets the bearing value, relative to North. Uses Angle Dimension.

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.semi_major_axis
    :type: float

    Defines the major axis for the ellipse. The value must be greater than 0. Uses Distance Dimension.

.. py:property:: semi_minor_axis
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.semi_minor_axis
    :type: float

    Defines the minor axis for the ellipse. The value must be greater than 0. Uses Distance Dimension.

.. py:property:: granularity
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.granularity
    :type: float

    Indicates the number of points used to draw the ellipse. Lower numbers create a better ellipse and higher numbers make the ellipse draw faster. Uses Angle Dimension.

.. py:property:: major_axis_offset
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.major_axis_offset
    :type: float

    Gets or sets the distance to offset the box (forward or backward) along the bearing. A positive MajorAxisOffset value moves the box forward. Uses Distance Dimension.

.. py:property:: minor_axis_offset
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse.minor_axis_offset
    :type: float

    Gets or sets the distance to offset the box (left or right) along the bearing. A positive MinorAxisOffset value moves the box to the right. Uses Distance Dimension.


