IVehicleGraphics3DBearingEllipse
================================

.. py:class:: IVehicleGraphics3DBearingEllipse

   IVehicleGraphics3DProximityAreaObject
   
   Define an ellipse, relative to a bearing from the North, around the object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~bearing`
            * - :py:meth:`~semi_major_axis`
            * - :py:meth:`~semi_minor_axis`
            * - :py:meth:`~granularity`
            * - :py:meth:`~major_axis_offset`
            * - :py:meth:`~minor_axis_offset`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DBearingEllipse


Property detail
---------------

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingEllipse.bearing
    :type: float

    Gets or sets the bearing value, relative to North. Uses Angle Dimension.

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingEllipse.semi_major_axis
    :type: float

    Defines the major axis for the ellipse. The value must be greater than 0. Uses Distance Dimension.

.. py:property:: semi_minor_axis
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingEllipse.semi_minor_axis
    :type: float

    Defines the minor axis for the ellipse. The value must be greater than 0. Uses Distance Dimension.

.. py:property:: granularity
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingEllipse.granularity
    :type: float

    Indicates the number of points used to draw the ellipse. Lower numbers create a better ellipse and higher numbers make the ellipse draw faster. Uses Angle Dimension.

.. py:property:: major_axis_offset
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingEllipse.major_axis_offset
    :type: float

    Gets or sets the distance to offset the box (forward or backward) along the bearing. A positive MajorAxisOffset value moves the box forward. Uses Distance Dimension.

.. py:property:: minor_axis_offset
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBearingEllipse.minor_axis_offset
    :type: float

    Gets or sets the distance to offset the box (left or right) along the bearing. A positive MinorAxisOffset value moves the box to the right. Uses Distance Dimension.


