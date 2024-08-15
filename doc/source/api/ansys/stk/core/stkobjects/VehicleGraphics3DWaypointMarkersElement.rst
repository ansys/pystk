VehicleGraphics3DWaypointMarkersElement
=======================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement

   3D waypoint.

.. py:currentmodule:: VehicleGraphics3DWaypointMarkersElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.set_image_file`
              - Set a file name of the image used for the waypoint.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.time`
              - Get the time of the waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.marker_type`
              - Get the marker type of the waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.shape`
              - Gets or sets the shape of the waypoint marker.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.marker_file`
              - Gets or sets the path and file name of the image used for the waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.pixel_size`
              - Gets or sets the pixel size of the waypoint marker. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.is_transparent`
              - Opt whether to use the color of the lower left pixel of the image as the transparent color if an image file is being used.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DWaypointMarkersElement


Property detail
---------------

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.time
    :type: typing.Any

    Get the time of the waypoint.

.. py:property:: marker_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.marker_type
    :type: ROUTE_GRAPHICS_3D_MARKER_TYPE

    Get the marker type of the waypoint.

.. py:property:: shape
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.shape
    :type: MARKER_SHAPE_3D

    Gets or sets the shape of the waypoint marker.

.. py:property:: marker_file
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.marker_file
    :type: str

    Gets or sets the path and file name of the image used for the waypoint.

.. py:property:: pixel_size
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.pixel_size
    :type: int

    Gets or sets the pixel size of the waypoint marker. Dimensionless.

.. py:property:: is_transparent
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.is_transparent
    :type: bool

    Opt whether to use the color of the lower left pixel of the image as the transparent color if an image file is being used.


Method detail
-------------












.. py:method:: set_image_file(self, markerFile: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.set_image_file

    Set a file name of the image used for the waypoint.

    :Parameters:

    **markerFile** : :obj:`~str`

    :Returns:

        :obj:`~None`

