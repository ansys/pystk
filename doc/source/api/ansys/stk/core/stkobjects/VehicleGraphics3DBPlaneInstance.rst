VehicleGraphics3DBPlaneInstance
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance

   An element in the IAgVeVOBPlanePointCollection.

.. py:currentmodule:: VehicleGraphics3DBPlaneInstance

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.show_graphics`
              - Whether the B-Plane will be displayed in the 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.name`
              - Gets or sets the name assigned to the B-Plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.description`
              - Gets or sets the description of the B-Plane instance.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.definition`
              - Get the template from which the B-Plane is derived.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.event_name`
              - Gets or sets the event name, which is the point in time at which the B-Plane is defined.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.event`
              - Returns the 3D BPlane Event properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.target_point`
              - Returns the 3D BPlane Target Point properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.show_label`
              - Whether to display all points with their appropriate labels.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.point_size`
              - Gets or sets the size at which to display all points on the B-Plane. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.connect_additional_points`
              - Whether to connect the additional points.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.connect_points_color`
              - Gets or sets the color of the lines connecting the additional points.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.connect_point_line_width`
              - Gets or sets the width of the lines connecting the additional points.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.graphics_3d_window`
              - Gets or sets the 3D Graphics windows in which the B-Plane will be displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.available_graphics_3d_windows`
              - Returns a list of available 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.additional_points`
              - Returns a collection of additional points.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DBPlaneInstance


Property detail
---------------

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.show_graphics
    :type: bool

    Whether the B-Plane will be displayed in the 3D Graphics window.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.name
    :type: str

    Gets or sets the name assigned to the B-Plane.

.. py:property:: description
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.description
    :type: str

    Gets or sets the description of the B-Plane instance.

.. py:property:: definition
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.definition
    :type: str

    Get the template from which the B-Plane is derived.

.. py:property:: event_name
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.event_name
    :type: str

    Gets or sets the event name, which is the point in time at which the B-Plane is defined.

.. py:property:: event
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.event
    :type: VehicleGraphics3DBPlaneEvent

    Returns the 3D BPlane Event properties.

.. py:property:: target_point
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.target_point
    :type: VehicleGraphics3DBPlaneTargetPoint

    Returns the 3D BPlane Target Point properties.

.. py:property:: show_label
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.show_label
    :type: bool

    Whether to display all points with their appropriate labels.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.point_size
    :type: float

    Gets or sets the size at which to display all points on the B-Plane. Dimensionless.

.. py:property:: connect_additional_points
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.connect_additional_points
    :type: bool

    Whether to connect the additional points.

.. py:property:: connect_points_color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.connect_points_color
    :type: agcolor.Color

    Gets or sets the color of the lines connecting the additional points.

.. py:property:: connect_point_line_width
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.connect_point_line_width
    :type: LineWidth

    Gets or sets the width of the lines connecting the additional points.

.. py:property:: graphics_3d_window
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.graphics_3d_window
    :type: str

    Gets or sets the 3D Graphics windows in which the B-Plane will be displayed.

.. py:property:: available_graphics_3d_windows
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.available_graphics_3d_windows
    :type: list

    Returns a list of available 3D Graphics windows.

.. py:property:: additional_points
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance.additional_points
    :type: VehicleGraphics3DBPlanePointCollection

    Returns a collection of additional points.


