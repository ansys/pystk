IVehicleGraphics3DBPlaneInstance
================================

.. py:class:: IVehicleGraphics3DBPlaneInstance

   object
   
   Properties of an instance of a B-Plane template.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~name`
            * - :py:meth:`~description`
            * - :py:meth:`~definition`
            * - :py:meth:`~event_name`
            * - :py:meth:`~event`
            * - :py:meth:`~target_point`
            * - :py:meth:`~is_label_visible`
            * - :py:meth:`~point_size`
            * - :py:meth:`~is_connect_points_visible`
            * - :py:meth:`~connect_points_color`
            * - :py:meth:`~connect_point_line_width`
            * - :py:meth:`~graphics_3d_window`
            * - :py:meth:`~available_graphics_3d_windows`
            * - :py:meth:`~additional_points`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DBPlaneInstance


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.is_visible
    :type: bool

    Whether the B-Plane will be displayed in the 3D Graphics window.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.name
    :type: str

    Gets or sets the name assigned to the B-Plane.

.. py:property:: description
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.description
    :type: str

    Gets or sets the description of the B-Plane instance.

.. py:property:: definition
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.definition
    :type: str

    Get the template from which the B-Plane is derived.

.. py:property:: event_name
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.event_name
    :type: str

    Gets or sets the event name, which is the point in time at which the B-Plane is defined.

.. py:property:: event
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.event
    :type: "IAgVeVOBPlaneEvent"

    Returns the 3D BPlane Event properties.

.. py:property:: target_point
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.target_point
    :type: "IAgVeVOBPlaneTargetPoint"

    Returns the 3D BPlane Target Point properties.

.. py:property:: is_label_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.is_label_visible
    :type: bool

    Whether to display all points with their appropriate labels.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.point_size
    :type: float

    Gets or sets the size at which to display all points on the B-Plane. Dimensionless.

.. py:property:: is_connect_points_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.is_connect_points_visible
    :type: bool

    Whether to connect the additional points.

.. py:property:: connect_points_color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.connect_points_color
    :type: agcolor.Color

    Gets or sets the color of the lines connecting the additional points.

.. py:property:: connect_point_line_width
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.connect_point_line_width
    :type: "LINE_WIDTH"

    Gets or sets the width of the lines connecting the additional points.

.. py:property:: graphics_3d_window
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.graphics_3d_window
    :type: str

    Gets or sets the 3D Graphics windows in which the B-Plane will be displayed.

.. py:property:: available_graphics_3d_windows
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.available_graphics_3d_windows
    :type: list

    Returns a list of available 3D Graphics windows.

.. py:property:: additional_points
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstance.additional_points
    :type: "IAgVeVOBPlanePointCollection"

    Returns a collection of additional points.


