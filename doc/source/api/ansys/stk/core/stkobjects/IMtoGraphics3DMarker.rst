IMtoGraphics3DMarker
====================

.. py:class:: IMtoGraphics3DMarker

   object
   
   Interface for MTO 3D graphics marker options.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_marker_image_file`
              - Set the marker image file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~pixel_size`
            * - :py:meth:`~marker_type`
            * - :py:meth:`~angle`
            * - :py:meth:`~x_origin`
            * - :py:meth:`~y_origin`
            * - :py:meth:`~marker_data`
            * - :py:meth:`~rotate_from_north`
            * - :py:meth:`~orientation_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics3DMarker


Property detail
---------------

.. py:property:: pixel_size
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DMarker.pixel_size
    :type: int

    The pixel size of the marker (markers do not resize as the window size is changed). Dimensionless.

.. py:property:: marker_type
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DMarker.marker_type
    :type: MARKER_TYPE

    Specify a 3D marker type to represent the object at the specified threshold. A member of the AgEMarkerType enumeration.

.. py:property:: angle
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DMarker.angle
    :type: typing.Any

    The angle representing the amount of rotation of the marker. Uses Angle Dimension.

.. py:property:: x_origin
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DMarker.x_origin
    :type: GRAPHICS_3D_MARKER_ORIGIN_TYPE

    The horizontal point of origin for the marker (left, center or right).

.. py:property:: y_origin
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DMarker.y_origin
    :type: GRAPHICS_3D_MARKER_ORIGIN_TYPE

    The vertical point of origin for the marker (top, center or bottom).

.. py:property:: marker_data
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DMarker.marker_data
    :type: IAgVOMarkerData

    The MarkerData property.

.. py:property:: rotate_from_north
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DMarker.rotate_from_north
    :type: bool

    Opt whether to set the rotation angle relative to north. (By default, the rotation angle is relative to the screen.).

.. py:property:: orientation_mode
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DMarker.orientation_mode
    :type: GRAPHICS_3D_MARKER_ORIENTATION

    Controls the rotation of the marker.


Method detail
-------------












.. py:method:: set_marker_image_file(self, imageFile: str) -> None
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DMarker.set_marker_image_file

    Set the marker image file.

    :Parameters:

    **imageFile** : :obj:`~str`

    :Returns:

        :obj:`~None`





