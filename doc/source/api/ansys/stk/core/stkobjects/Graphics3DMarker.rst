Graphics3DMarker
================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DMarker

   Class defining the 3D marker to represent an object at a specified threshold.

.. py:currentmodule:: Graphics3DMarker

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarker.set_marker_image_filename`
              - Set the marker image file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarker.pixel_size`
              - The pixel size of the marker. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarker.visible`
              - Display a marker in the 3D Graphics window at the object position for the object once a specified detail threshold has been crossed.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarker.marker_type`
              - Specify a 3D marker type to represent the object at the specified threshold. Setting the type with the enum eImageFile is invalid, use SetMarkerImageFile instead.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarker.angle`
              - The angle representing the amount of rotation of the marker. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarker.x_origin`
              - The horizontal point of origin for the marker (left, center or right).
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarker.y_origin`
              - The vertical point of origin for the marker (top, center or bottom.).
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarker.marker_data`
              - The MarkerData property.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarker.orientation_mode`
              - Controls the rotation of the marker.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DMarker


Property detail
---------------

.. py:property:: pixel_size
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarker.pixel_size
    :type: int

    The pixel size of the marker. Dimensionless.

.. py:property:: visible
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarker.visible
    :type: bool

    Display a marker in the 3D Graphics window at the object position for the object once a specified detail threshold has been crossed.

.. py:property:: marker_type
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarker.marker_type
    :type: MARKER_TYPE

    Specify a 3D marker type to represent the object at the specified threshold. Setting the type with the enum eImageFile is invalid, use SetMarkerImageFile instead.

.. py:property:: angle
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarker.angle
    :type: typing.Any

    The angle representing the amount of rotation of the marker. Uses Angle Dimension.

.. py:property:: x_origin
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarker.x_origin
    :type: GRAPHICS_3D_MARKER_ORIGIN_TYPE

    The horizontal point of origin for the marker (left, center or right).

.. py:property:: y_origin
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarker.y_origin
    :type: GRAPHICS_3D_MARKER_ORIGIN_TYPE

    The vertical point of origin for the marker (top, center or bottom.).

.. py:property:: marker_data
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarker.marker_data
    :type: IGraphics3DMarkerData

    The MarkerData property.

.. py:property:: orientation_mode
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarker.orientation_mode
    :type: GRAPHICS_3D_MARKER_ORIENTATION

    Controls the rotation of the marker.


Method detail
-------------














.. py:method:: set_marker_image_filename(self, imageFile: str) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarker.set_marker_image_filename

    Set the marker image file.

    :Parameters:

    **imageFile** : :obj:`~str`

    :Returns:

        :obj:`~None`



