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
              - Get or set the shape of the waypoint marker.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.marker_filename`
              - Get or set the path and file name of the image used for the waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.pixel_size`
              - Get or set the pixel size of the waypoint marker. Dimensionless.
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
    :type: RouteGraphics3DMarkerType

    Get the marker type of the waypoint.

.. py:property:: shape
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.shape
    :type: MarkerShape3d

    Get or set the shape of the waypoint marker.

.. py:property:: marker_filename
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.marker_filename
    :type: str

    Get or set the path and file name of the image used for the waypoint.

.. py:property:: pixel_size
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.pixel_size
    :type: int

    Get or set the pixel size of the waypoint marker. Dimensionless.

.. py:property:: is_transparent
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.is_transparent
    :type: bool

    Opt whether to use the color of the lower left pixel of the image as the transparent color if an image file is being used.


Method detail
-------------












.. py:method:: set_image_file(self, marker_file: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement.set_image_file

    Set a file name of the image used for the waypoint.

    :Parameters:

        **marker_file** : :obj:`~str`


    :Returns:

        :obj:`~None`

