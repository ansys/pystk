Camera
======

.. py:class:: ansys.stk.core.graphics.Camera

   Implemented by the scene camera. Contains operations to manipulate the camera position, view direction and orientation in the scene.

.. py:currentmodule:: Camera

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.Camera.visibility_test`
              - Get the visibility of a sphere against the view frustum and any occluding central bodies.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.cartographic_to_window`
              - Convert a cartographic position to a pixel coordinate relative to the globe control. This method can throw an exception. Returns an array containing the pixel coordinate (in the order x, y) of the cartographic position relative to the globe control...
            * - :py:attr:`~ansys.stk.core.graphics.Camera.try_cartographic_to_window`
              - Convert a cartographic position to a pixel coordinate relative to the globe control. This method does not throw an exception.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.window_to_cartographic`
              - Convert a pixel coordinate relative to the globe control to a cartographic position. For speed, terrain is not considered; if the pixel coordinate does not intersect the ellipsoid, an exception is thrown. Returns the cartographic position...
            * - :py:attr:`~ansys.stk.core.graphics.Camera.try_window_to_cartographic`
              - Convert a pixel coordinate relative to the globe control to a cartographic position. For speed, terrain is not considered. This method does not throw an exception.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.view_central_body`
              - Zoom to a central body and use the specified axes for rotation. The reference point is set to the center of the central body and the camera's position is set so the entire central body is visible.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.view_extent`
              - Zooms to a cartographic extent on the centralBody. The camera will be looking straight down at the extent, with the up vector pointing toward local north. The axes is set to an east-north-up axes at the center of extent.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.view_rectangular_extent`
              - Zooms to a rectangular extent composed of west, south, east, north on the centralBody. The camera will be looking straight down at the extent, with the up vector pointing toward local north...
            * - :py:attr:`~ansys.stk.core.graphics.Camera.view_with_up_axis`
              - View from a point to a point. Sets the camera's position and the reference point the camera is looking at.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.view`
              - View from a point to a point. Sets the camera's position and the reference point the camera is looking at.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.view_direction_with_up_axis`
              - View from a point to a direction. Sets the camera's position and the direction vector indicating where the camera is looking.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.view_direction`
              - View from a point to a direction. Sets the camera's position and the direction vector indicating where the camera is looking.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.view_offset_with_up_axis`
              - Set the camera's reference point - the point the camera is looking at. The camera's position is the reference point translated by the offset.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.view_offset`
              - Set the camera's reference point - the point the camera is looking at. The camera's position is the reference point translated by the offset.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.view_offset_direction_with_up_axis`
              - Set the camera's reference point - the point the camera is looking at. The camera's position is the reference point translated by the direction vector.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.view_offset_direction`
              - Set the camera's reference point - the point the camera is looking at. The camera's position is the reference point translated by the direction vector.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.Camera.position`
              - Gets or sets the position of the camera. The array contains the components of the position arranged in the order x, y, z.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.reference_point`
              - Gets or sets the reference point of the camera. The array contains the components of the reference point arranged in the order x, y, z.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.direction`
              - Gets or sets the direction of the camera in axes. The array contains the components of the direction arranged in the order x, y, z.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.up_vector`
              - Gets or sets the up direction of the camera in axes. The array contains the components of the direction arranged in the order x, y, z.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.distance`
              - Gets or sets the distance the camera position is from the reference point.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.axes`
              - Gets or sets camera's axes of rotation.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.constrained_up_axis`
              - Gets or sets the axis to constrain the up vector to.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.allow_rotation_over_constrained_up_axis`
              - Gets or sets whether the camera can rotate over the constrained up axis. For example, if true the camera would be able to flip over the North Pole and view the globe upside down.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.lock_view_direction`
              - Gets or sets whether the camera's direction is locked.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.field_of_view`
              - Gets or sets field of view. The field of view is applied to the larger of the window dimensions. For example, if the window width was 640 and the height was 480, the field of view applies to the horizontal...
            * - :py:attr:`~ansys.stk.core.graphics.Camera.horizontal_field_of_view`
              - Gets the horizontal field of view.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.vertical_field_of_view`
              - Gets the vertical field of view.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.near_plane`
              - Gets or sets the distance from the camera to the near plane.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.far_plane`
              - Gets or sets the distance from the camera to the far plane.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.far_near_plane_ratio`
              - Gets or sets the value that is used to compute subdivisions of the viewing frustum. A large value will be faster but lose z-value precision. A small value will have better precision but perform slower...
            * - :py:attr:`~ansys.stk.core.graphics.Camera.distance_per_radius`
              - Returns the distance that the Camera's Position should be from the ReferencePoint in order to ensure that a sphere with a 1 meter radius centered at the ReferencePoint fits entirely in the view frustum.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.snapshot`
              - Gets the camera snapshot settings.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.video_recording`
              - Gets the camera video recorder.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.pixel_size_per_distance`
              - Gets the approximate number of meters covered by a pixel that is 1 meter away from the camera. This is commonly multiplied by the distance from the camera to an object to compute the approximate number of meters covered by a pixel of the object.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.position_reference_frame`
              - Gets the reference frame that the position is returned in. This reference frame is composed of the camera's from point and the axes.
            * - :py:attr:`~ansys.stk.core.graphics.Camera.reference_point_reference_frame`
              - Gets the reference frame that the reference point is returned in. This reference frame is composed of the camera's to point and the axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import Camera


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.graphics.Camera.position
    :type: list

    Gets or sets the position of the camera. The array contains the components of the position arranged in the order x, y, z.

.. py:property:: reference_point
    :canonical: ansys.stk.core.graphics.Camera.reference_point
    :type: list

    Gets or sets the reference point of the camera. The array contains the components of the reference point arranged in the order x, y, z.

.. py:property:: direction
    :canonical: ansys.stk.core.graphics.Camera.direction
    :type: list

    Gets or sets the direction of the camera in axes. The array contains the components of the direction arranged in the order x, y, z.

.. py:property:: up_vector
    :canonical: ansys.stk.core.graphics.Camera.up_vector
    :type: list

    Gets or sets the up direction of the camera in axes. The array contains the components of the direction arranged in the order x, y, z.

.. py:property:: distance
    :canonical: ansys.stk.core.graphics.Camera.distance
    :type: float

    Gets or sets the distance the camera position is from the reference point.

.. py:property:: axes
    :canonical: ansys.stk.core.graphics.Camera.axes
    :type: IVectorGeometryToolAxes

    Gets or sets camera's axes of rotation.

.. py:property:: constrained_up_axis
    :canonical: ansys.stk.core.graphics.Camera.constrained_up_axis
    :type: CONSTRAINED_UP_AXIS

    Gets or sets the axis to constrain the up vector to.

.. py:property:: allow_rotation_over_constrained_up_axis
    :canonical: ansys.stk.core.graphics.Camera.allow_rotation_over_constrained_up_axis
    :type: bool

    Gets or sets whether the camera can rotate over the constrained up axis. For example, if true the camera would be able to flip over the North Pole and view the globe upside down.

.. py:property:: lock_view_direction
    :canonical: ansys.stk.core.graphics.Camera.lock_view_direction
    :type: bool

    Gets or sets whether the camera's direction is locked.

.. py:property:: field_of_view
    :canonical: ansys.stk.core.graphics.Camera.field_of_view
    :type: float

    Gets or sets field of view. The field of view is applied to the larger of the window dimensions. For example, if the window width was 640 and the height was 480, the field of view applies to the horizontal...

.. py:property:: horizontal_field_of_view
    :canonical: ansys.stk.core.graphics.Camera.horizontal_field_of_view
    :type: float

    Gets the horizontal field of view.

.. py:property:: vertical_field_of_view
    :canonical: ansys.stk.core.graphics.Camera.vertical_field_of_view
    :type: float

    Gets the vertical field of view.

.. py:property:: near_plane
    :canonical: ansys.stk.core.graphics.Camera.near_plane
    :type: float

    Gets or sets the distance from the camera to the near plane.

.. py:property:: far_plane
    :canonical: ansys.stk.core.graphics.Camera.far_plane
    :type: float

    Gets or sets the distance from the camera to the far plane.

.. py:property:: far_near_plane_ratio
    :canonical: ansys.stk.core.graphics.Camera.far_near_plane_ratio
    :type: float

    Gets or sets the value that is used to compute subdivisions of the viewing frustum. A large value will be faster but lose z-value precision. A small value will have better precision but perform slower...

.. py:property:: distance_per_radius
    :canonical: ansys.stk.core.graphics.Camera.distance_per_radius
    :type: float

    Returns the distance that the Camera's Position should be from the ReferencePoint in order to ensure that a sphere with a 1 meter radius centered at the ReferencePoint fits entirely in the view frustum.

.. py:property:: snapshot
    :canonical: ansys.stk.core.graphics.Camera.snapshot
    :type: CameraSnapshot

    Gets the camera snapshot settings.

.. py:property:: video_recording
    :canonical: ansys.stk.core.graphics.Camera.video_recording
    :type: CameraVideoRecording

    Gets the camera video recorder.

.. py:property:: pixel_size_per_distance
    :canonical: ansys.stk.core.graphics.Camera.pixel_size_per_distance
    :type: float

    Gets the approximate number of meters covered by a pixel that is 1 meter away from the camera. This is commonly multiplied by the distance from the camera to an object to compute the approximate number of meters covered by a pixel of the object.

.. py:property:: position_reference_frame
    :canonical: ansys.stk.core.graphics.Camera.position_reference_frame
    :type: IVectorGeometryToolSystem

    Gets the reference frame that the position is returned in. This reference frame is composed of the camera's from point and the axes.

.. py:property:: reference_point_reference_frame
    :canonical: ansys.stk.core.graphics.Camera.reference_point_reference_frame
    :type: IVectorGeometryToolSystem

    Gets the reference frame that the reference point is returned in. This reference frame is composed of the camera's to point and the axes.


Method detail
-------------



































.. py:method:: visibility_test(self, reference_frame: IVectorGeometryToolSystem, sphere: BoundingSphere) -> VISIBILITY
    :canonical: ansys.stk.core.graphics.Camera.visibility_test

    Get the visibility of a sphere against the view frustum and any occluding central bodies.

    :Parameters:

    **reference_frame** : :obj:`~IVectorGeometryToolSystem`
    **sphere** : :obj:`~BoundingSphere`

    :Returns:

        :obj:`~VISIBILITY`

.. py:method:: cartographic_to_window(self, central_body: str, position: list) -> list
    :canonical: ansys.stk.core.graphics.Camera.cartographic_to_window

    Convert a cartographic position to a pixel coordinate relative to the globe control. This method can throw an exception. Returns an array containing the pixel coordinate (in the order x, y) of the cartographic position relative to the globe control...

    :Parameters:

    **central_body** : :obj:`~str`
    **position** : :obj:`~list`

    :Returns:

        :obj:`~list`

.. py:method:: try_cartographic_to_window(self, central_body: str, position: list) -> list
    :canonical: ansys.stk.core.graphics.Camera.try_cartographic_to_window

    Convert a cartographic position to a pixel coordinate relative to the globe control. This method does not throw an exception.

    :Parameters:

    **central_body** : :obj:`~str`
    **position** : :obj:`~list`

    :Returns:

        :obj:`~list`

.. py:method:: window_to_cartographic(self, central_body: str, position: list) -> list
    :canonical: ansys.stk.core.graphics.Camera.window_to_cartographic

    Convert a pixel coordinate relative to the globe control to a cartographic position. For speed, terrain is not considered; if the pixel coordinate does not intersect the ellipsoid, an exception is thrown. Returns the cartographic position...

    :Parameters:

    **central_body** : :obj:`~str`
    **position** : :obj:`~list`

    :Returns:

        :obj:`~list`

.. py:method:: try_window_to_cartographic(self, central_body: str, position: list) -> list
    :canonical: ansys.stk.core.graphics.Camera.try_window_to_cartographic

    Convert a pixel coordinate relative to the globe control to a cartographic position. For speed, terrain is not considered. This method does not throw an exception.

    :Parameters:

    **central_body** : :obj:`~str`
    **position** : :obj:`~list`

    :Returns:

        :obj:`~list`

.. py:method:: view_central_body(self, central_body: str, axes: IVectorGeometryToolAxes) -> None
    :canonical: ansys.stk.core.graphics.Camera.view_central_body

    Zoom to a central body and use the specified axes for rotation. The reference point is set to the center of the central body and the camera's position is set so the entire central body is visible.

    :Parameters:

    **central_body** : :obj:`~str`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~None`

.. py:method:: view_extent(self, central_body: str, extent: list) -> None
    :canonical: ansys.stk.core.graphics.Camera.view_extent

    Zooms to a cartographic extent on the centralBody. The camera will be looking straight down at the extent, with the up vector pointing toward local north. The axes is set to an east-north-up axes at the center of extent.

    :Parameters:

    **central_body** : :obj:`~str`
    **extent** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: view_rectangular_extent(self, central_body: str, west: float, south: float, east: float, north: float) -> None
    :canonical: ansys.stk.core.graphics.Camera.view_rectangular_extent

    Zooms to a rectangular extent composed of west, south, east, north on the centralBody. The camera will be looking straight down at the extent, with the up vector pointing toward local north...

    :Parameters:

    **central_body** : :obj:`~str`
    **west** : :obj:`~float`
    **south** : :obj:`~float`
    **east** : :obj:`~float`
    **north** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: view_with_up_axis(self, axes: IVectorGeometryToolAxes, camera_position: IVectorGeometryToolPoint, reference_point: IVectorGeometryToolPoint, up_axis: list) -> None
    :canonical: ansys.stk.core.graphics.Camera.view_with_up_axis

    View from a point to a point. Sets the camera's position and the reference point the camera is looking at.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`
    **camera_position** : :obj:`~IVectorGeometryToolPoint`
    **reference_point** : :obj:`~IVectorGeometryToolPoint`
    **up_axis** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: view(self, axes: IVectorGeometryToolAxes, camera_position: IVectorGeometryToolPoint, reference_point: IVectorGeometryToolPoint) -> None
    :canonical: ansys.stk.core.graphics.Camera.view

    View from a point to a point. Sets the camera's position and the reference point the camera is looking at.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`
    **camera_position** : :obj:`~IVectorGeometryToolPoint`
    **reference_point** : :obj:`~IVectorGeometryToolPoint`

    :Returns:

        :obj:`~None`

.. py:method:: view_direction_with_up_axis(self, axes: IVectorGeometryToolAxes, camera_position: IVectorGeometryToolPoint, direction: IVectorGeometryToolVector, up_axis: list) -> None
    :canonical: ansys.stk.core.graphics.Camera.view_direction_with_up_axis

    View from a point to a direction. Sets the camera's position and the direction vector indicating where the camera is looking.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`
    **camera_position** : :obj:`~IVectorGeometryToolPoint`
    **direction** : :obj:`~IVectorGeometryToolVector`
    **up_axis** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: view_direction(self, axes: IVectorGeometryToolAxes, camera_position: IVectorGeometryToolPoint, direction: IVectorGeometryToolVector) -> None
    :canonical: ansys.stk.core.graphics.Camera.view_direction

    View from a point to a direction. Sets the camera's position and the direction vector indicating where the camera is looking.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`
    **camera_position** : :obj:`~IVectorGeometryToolPoint`
    **direction** : :obj:`~IVectorGeometryToolVector`

    :Returns:

        :obj:`~None`

.. py:method:: view_offset_with_up_axis(self, axes: IVectorGeometryToolAxes, reference_point: IVectorGeometryToolPoint, offset: list, up_axis: list) -> None
    :canonical: ansys.stk.core.graphics.Camera.view_offset_with_up_axis

    Set the camera's reference point - the point the camera is looking at. The camera's position is the reference point translated by the offset.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`
    **reference_point** : :obj:`~IVectorGeometryToolPoint`
    **offset** : :obj:`~list`
    **up_axis** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: view_offset(self, axes: IVectorGeometryToolAxes, reference_point: IVectorGeometryToolPoint, offset: list) -> None
    :canonical: ansys.stk.core.graphics.Camera.view_offset

    Set the camera's reference point - the point the camera is looking at. The camera's position is the reference point translated by the offset.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`
    **reference_point** : :obj:`~IVectorGeometryToolPoint`
    **offset** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: view_offset_direction_with_up_axis(self, axes: IVectorGeometryToolAxes, reference_point: IVectorGeometryToolPoint, direction: IVectorGeometryToolVector, up_axis: list) -> None
    :canonical: ansys.stk.core.graphics.Camera.view_offset_direction_with_up_axis

    Set the camera's reference point - the point the camera is looking at. The camera's position is the reference point translated by the direction vector.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`
    **reference_point** : :obj:`~IVectorGeometryToolPoint`
    **direction** : :obj:`~IVectorGeometryToolVector`
    **up_axis** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: view_offset_direction(self, axes: IVectorGeometryToolAxes, reference_point: IVectorGeometryToolPoint, direction: IVectorGeometryToolVector) -> None
    :canonical: ansys.stk.core.graphics.Camera.view_offset_direction

    Set the camera's reference point - the point the camera is looking at. The camera's position is the reference point translated by the direction vector.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`
    **reference_point** : :obj:`~IVectorGeometryToolPoint`
    **direction** : :obj:`~IVectorGeometryToolVector`

    :Returns:

        :obj:`~None`

