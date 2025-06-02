MTOGraphics3DMarker
===================

.. py:class:: ansys.stk.core.stkobjects.MTOGraphics3DMarker

   MTO 3D graphics marker options.

.. py:currentmodule:: MTOGraphics3DMarker

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DMarker.set_marker_image_filename`
              - Set the marker image file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DMarker.pixel_size`
              - The pixel size of the marker (markers do not resize as the window size is changed). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DMarker.marker_type`
              - Specify a 3D marker type to represent the object at the specified threshold. A member of the MarkerType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DMarker.angle`
              - The angle representing the amount of rotation of the marker. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DMarker.x_origin`
              - The horizontal point of origin for the marker (left, center or right).
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DMarker.y_origin`
              - The vertical point of origin for the marker (top, center or bottom).
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DMarker.marker_data`
              - The MarkerData property.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DMarker.rotate_from_north`
              - Opt whether to set the rotation angle relative to north. (By default, the rotation angle is relative to the screen.).
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics3DMarker.orientation_mode`
              - Control the rotation of the marker.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOGraphics3DMarker


Property detail
---------------

.. py:property:: pixel_size
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DMarker.pixel_size
    :type: int

    The pixel size of the marker (markers do not resize as the window size is changed). Dimensionless.

.. py:property:: marker_type
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DMarker.marker_type
    :type: MarkerType

    Specify a 3D marker type to represent the object at the specified threshold. A member of the MarkerType enumeration.

.. py:property:: angle
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DMarker.angle
    :type: typing.Any

    The angle representing the amount of rotation of the marker. Uses Angle Dimension.

.. py:property:: x_origin
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DMarker.x_origin
    :type: Graphics3DMarkerOriginType

    The horizontal point of origin for the marker (left, center or right).

.. py:property:: y_origin
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DMarker.y_origin
    :type: Graphics3DMarkerOriginType

    The vertical point of origin for the marker (top, center or bottom).

.. py:property:: marker_data
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DMarker.marker_data
    :type: IGraphics3DMarkerData

    The MarkerData property.

.. py:property:: rotate_from_north
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DMarker.rotate_from_north
    :type: bool

    Opt whether to set the rotation angle relative to north. (By default, the rotation angle is relative to the screen.).

.. py:property:: orientation_mode
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DMarker.orientation_mode
    :type: Graphics3DMarkerOrientation

    Control the rotation of the marker.


Method detail
-------------












.. py:method:: set_marker_image_filename(self, image_file: str) -> None
    :canonical: ansys.stk.core.stkobjects.MTOGraphics3DMarker.set_marker_image_filename

    Set the marker image file.

    :Parameters:

        **image_file** : :obj:`~str`


    :Returns:

        :obj:`~None`





