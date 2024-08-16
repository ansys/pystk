UiAx2DCntrl
===========

.. py:class:: ansys.stk.core.stkx.UiAx2DCntrl

   AGI Map control.

.. py:currentmodule:: UiAx2DCntrl

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.picture_put_reference`
              - Set a reference to the splash logo graphic to be displayed in the control.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.zoom_in`
              - Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.zoom_out`
              - Zoom out to view a larger portion of a previously magnified map.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.pick_info`
              - Get detailed information about a mouse pick.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.copy_from_win_id`
              - Copy an existing Window's scene into this control.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.rubber_band_pick_info`
              - Get detailed information about a rubber-band mouse pick. The values must be within the 2D window (0 to width-1 for left and right, 0 to height-1 for top and bottom).
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.get_window_projected_position`
              - Get the window projected position for given values.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.set_mouse_cursor_from_file`
              - Set mouse cursor to the selected cursor file.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.restore_mouse_cursor`
              - Restores mouse cursor back to normal.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.set_mouse_cursor_from_handle`
              - Set mouse cursor to the passed cursor handle.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.Subscribe`
              - """Return an IUiAxGraphics2DCntrlEventHandler that is subscribed to handle events associated with this instance of UiAx2DCntrl."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.back_color`
              - The background color of the control.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.picture`
              - The splash logo graphic to be displayed in the control.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.win_id`
              - Window identifier (for Connect commands).
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.application`
              - Reference to the STK X application object.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.no_logo`
              - If true, the splash logo is not shown.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.ole_drop_mode`
              - How the control handles drop operations.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.vendor_id`
              - This property is deprecated. The identifier of the vendor.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.mouse_mode`
              - Whether this control responds to mouse events.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.ready_state`
              - Returns/sets the background color of the control.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.advanced_pick_mode`
              - If true, sets the advance pick mode.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.in_zoom_mode`
              - Returns true if in zoom in mode.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.show_progress_image`
              - The animated progress image type.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.progress_image_x_offset`
              - The horizontal X offset for animated progress image.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.progress_image_y_offset`
              - The vertical Y offset for animated progress image.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.progress_image_file`
              - The complete image file name/path for animated progress image.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.progress_image_x_origin`
              - The X origin alignment for animated progress image.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.progress_image_y_origin`
              - The Y origin alignment for animated progress image.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.picture_from_file`
              - Gets or sets the splash logo graphic file to be displayed in the control.
            * - :py:attr:`~ansys.stk.core.stkx.UiAx2DCntrl.pan_mode_enabled`
              - Enables/disables pan mode for map control.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import UiAx2DCntrl


Property detail
---------------

.. py:property:: back_color
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.back_color
    :type: agcolor.Color

    The background color of the control.

.. py:property:: picture
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.picture
    :type: IPictureDisp

    The splash logo graphic to be displayed in the control.

.. py:property:: win_id
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.win_id
    :type: int

    Window identifier (for Connect commands).

.. py:property:: application
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.application
    :type: STKXApplication

    Reference to the STK X application object.

.. py:property:: no_logo
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.no_logo
    :type: bool

    If true, the splash logo is not shown.

.. py:property:: ole_drop_mode
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.ole_drop_mode
    :type: OLE_DROP_MODE

    How the control handles drop operations.

.. py:property:: vendor_id
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.vendor_id
    :type: str

    This property is deprecated. The identifier of the vendor.

.. py:property:: mouse_mode
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.mouse_mode
    :type: MOUSE_MODE

    Whether this control responds to mouse events.

.. py:property:: ready_state
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.ready_state
    :type: int

    Returns/sets the background color of the control.

.. py:property:: advanced_pick_mode
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.advanced_pick_mode
    :type: bool

    If true, sets the advance pick mode.

.. py:property:: in_zoom_mode
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.in_zoom_mode
    :type: bool

    Returns true if in zoom in mode.

.. py:property:: show_progress_image
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.show_progress_image
    :type: SHOW_PROGRESS_IMAGE

    The animated progress image type.

.. py:property:: progress_image_x_offset
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.progress_image_x_offset
    :type: int

    The horizontal X offset for animated progress image.

.. py:property:: progress_image_y_offset
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.progress_image_y_offset
    :type: int

    The vertical Y offset for animated progress image.

.. py:property:: progress_image_file
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.progress_image_file
    :type: str

    The complete image file name/path for animated progress image.

.. py:property:: progress_image_x_origin
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.progress_image_x_origin
    :type: PROGRESS_IMAGE_X_ORIGIN

    The X origin alignment for animated progress image.

.. py:property:: progress_image_y_origin
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.progress_image_y_origin
    :type: PROGRESS_IMAGE_Y_ORIGIN

    The Y origin alignment for animated progress image.

.. py:property:: picture_from_file
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.picture_from_file
    :type: str

    Gets or sets the splash logo graphic file to be displayed in the control.

.. py:property:: pan_mode_enabled
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.pan_mode_enabled
    :type: bool

    Enables/disables pan mode for map control.


Method detail
-------------




.. py:method:: picture_put_reference(self, pPicture: IPictureDisp) -> None
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.picture_put_reference

    Set a reference to the splash logo graphic to be displayed in the control.

    :Parameters:

    **pPicture** : :obj:`~IPictureDisp`

    :Returns:

        :obj:`~None`




.. py:method:: zoom_in(self) -> None
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.zoom_in

    Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom.

    :Returns:

        :obj:`~None`

.. py:method:: zoom_out(self) -> None
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.zoom_out

    Zoom out to view a larger portion of a previously magnified map.

    :Returns:

        :obj:`~None`

.. py:method:: pick_info(self, x: int, y: int) -> PickInfoData
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.pick_info

    Get detailed information about a mouse pick.

    :Parameters:

    **x** : :obj:`~int`
    **y** : :obj:`~int`

    :Returns:

        :obj:`~PickInfoData`











.. py:method:: copy_from_win_id(self, winID: int) -> None
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.copy_from_win_id

    Copy an existing Window's scene into this control.

    :Parameters:

    **winID** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: rubber_band_pick_info(self, left: int, top: int, right: int, bottom: int) -> RubberBandPickInfoData
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.rubber_band_pick_info

    Get detailed information about a rubber-band mouse pick. The values must be within the 2D window (0 to width-1 for left and right, 0 to height-1 for top and bottom).

    :Parameters:

    **left** : :obj:`~int`
    **top** : :obj:`~int`
    **right** : :obj:`~int`
    **bottom** : :obj:`~int`

    :Returns:

        :obj:`~RubberBandPickInfoData`



.. py:method:: get_window_projected_position(self, lat: float, lon: float, alt: float, drawCoords: GRAPHICS_2D_DRAW_COORDS) -> WinProjectionPosition
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.get_window_projected_position

    Get the window projected position for given values.

    :Parameters:

    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`
    **drawCoords** : :obj:`~GRAPHICS_2D_DRAW_COORDS`

    :Returns:

        :obj:`~WinProjectionPosition`


.. py:method:: set_mouse_cursor_from_file(self, cursorFileName: str) -> None
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.set_mouse_cursor_from_file

    Set mouse cursor to the selected cursor file.

    :Parameters:

    **cursorFileName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: restore_mouse_cursor(self) -> None
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.restore_mouse_cursor

    Restores mouse cursor back to normal.

    :Returns:

        :obj:`~None`

.. py:method:: set_mouse_cursor_from_handle(self, cursorHandle: int) -> None
    :canonical: ansys.stk.core.stkx.UiAx2DCntrl.set_mouse_cursor_from_handle

    Set mouse cursor to the passed cursor handle.

    :Parameters:

    **cursorHandle** : :obj:`~int`

    :Returns:

        :obj:`~None`

















