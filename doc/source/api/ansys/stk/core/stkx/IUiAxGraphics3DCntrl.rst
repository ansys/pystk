IUiAxGraphics3DCntrl
====================

.. py:class:: ansys.stk.core.stkx.IUiAxGraphics3DCntrl

   object
   
   AGI Globe control.

.. py:currentmodule:: IUiAxGraphics3DCntrl

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.picture_put_reference`
              - Set a reference to the splash logo graphic to be displayed in the control.
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.pick_info`
              - Get detailed information about a mouse pick.
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.zoom_in`
              - Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom.
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.rubber_band_pick_info`
              - Get detailed information about a rubber-band mouse pick. The values must be within the VO window (0 to width-1 for left and right, 0 to height-1 for top and bottom).
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.copy_from_win_id`
              - Copy an existing Window's scene into this control.
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.start_object_editing`
              - Enters into 3D object editing mode.
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.apply_object_editing`
              - Commit changes when in 3D object editing mode.
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.stop_object_editing`
              - End 3D object editing mode.
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.set_mouse_cursor_from_file`
              - Set mouse cursor to the selected cursor file.
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.restore_mouse_cursor`
              - Restores mouse cursor back to normal.
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.set_mouse_cursor_from_handle`
              - Set mouse cursor to the passed cursor handle.
            * - :py:attr:`~Subscribe`
              - """Return an IUiAxGraphics3DCntrlEventHandler that is subscribed to handle events associated with this instance of IUiAxGraphics3DCntrl."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.back_color`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.picture`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.win_id`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.application`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.no_logo`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.ole_drop_mode`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.vendor_id`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.mouse_mode`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.draw_elements`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.ready_state`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.ppt_preload_mode`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.advanced_pick_mode`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.is_object_editing`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.in_zoom_mode`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.show_progress_image`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.progress_image_x_offset`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.progress_image_y_offset`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.progress_image_file`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.progress_image_x_origin`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.progress_image_y_origin`
            * - :py:attr:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl.picture_from_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import IUiAxGraphics3DCntrl


Property detail
---------------

.. py:property:: back_color
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.back_color
    :type: agcolor.Color

    The background color of the control.

.. py:property:: picture
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.picture
    :type: IPictureDisp

    The splash logo graphic to be displayed in the control.

.. py:property:: win_id
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.win_id
    :type: int

    Window identifier (for Connect commands).

.. py:property:: application
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.application
    :type: ISTKXApplication

    Reference to the STK X application object.

.. py:property:: no_logo
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.no_logo
    :type: bool

    If true, the splash logo is not shown.

.. py:property:: ole_drop_mode
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.ole_drop_mode
    :type: OLE_DROP_MODE

    How the control handles drop operations.

.. py:property:: vendor_id
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.vendor_id
    :type: str

    This property is deprecated. The identifier of the vendor.

.. py:property:: mouse_mode
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.mouse_mode
    :type: MOUSE_MODE

    Whether this control responds to mouse events.

.. py:property:: draw_elements
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.draw_elements
    :type: IDrawElemCollection

    Elements to draw on the control.

.. py:property:: ready_state
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.ready_state
    :type: int

    Returns/sets the background color of the control.

.. py:property:: ppt_preload_mode
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.ppt_preload_mode
    :type: bool

    Special mode for PowerPoint : if true the VO control window is kept around when switching between slides.

.. py:property:: advanced_pick_mode
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.advanced_pick_mode
    :type: bool

    If true, sets the advance pick mode.

.. py:property:: is_object_editing
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.is_object_editing
    :type: bool

    Returns true if in 3D object editing mode.

.. py:property:: in_zoom_mode
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.in_zoom_mode
    :type: bool

    Returns true if in zoom in mode.

.. py:property:: show_progress_image
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.show_progress_image
    :type: SHOW_PROGRESS_IMAGE

    The animated progress image type.

.. py:property:: progress_image_x_offset
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.progress_image_x_offset
    :type: int

    The horizontal X offset for animated progress image.

.. py:property:: progress_image_y_offset
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.progress_image_y_offset
    :type: int

    The vertical Y offset for animated progress image.

.. py:property:: progress_image_file
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.progress_image_file
    :type: str

    The complete image file name/path for animated progress image.

.. py:property:: progress_image_x_origin
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.progress_image_x_origin
    :type: PROGRESS_IMAGE_X_ORIGIN

    The X origin alignment for animated progress image.

.. py:property:: progress_image_y_origin
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.progress_image_y_origin
    :type: PROGRESS_IMAGE_Y_ORIGIN

    The Y origin alignment for animated progress image.

.. py:property:: picture_from_file
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.picture_from_file
    :type: str

    Gets or sets the splash logo graphic file to be displayed in the control.


Method detail
-------------




.. py:method:: picture_put_reference(self, pPicture: IPictureDisp) -> None
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.picture_put_reference

    Set a reference to the splash logo graphic to be displayed in the control.

    :Parameters:

    **pPicture** : :obj:`~IPictureDisp`

    :Returns:

        :obj:`~None`


.. py:method:: pick_info(self, x: int, y: int) -> IPickInfoData
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.pick_info

    Get detailed information about a mouse pick.

    :Parameters:

    **x** : :obj:`~int`
    **y** : :obj:`~int`

    :Returns:

        :obj:`~IPickInfoData`




.. py:method:: zoom_in(self) -> None
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.zoom_in

    Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom.

    :Returns:

        :obj:`~None`







.. py:method:: rubber_band_pick_info(self, left: int, top: int, right: int, bottom: int) -> IRubberBandPickInfoData
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.rubber_band_pick_info

    Get detailed information about a rubber-band mouse pick. The values must be within the VO window (0 to width-1 for left and right, 0 to height-1 for top and bottom).

    :Parameters:

    **left** : :obj:`~int`
    **top** : :obj:`~int`
    **right** : :obj:`~int`
    **bottom** : :obj:`~int`

    :Returns:

        :obj:`~IRubberBandPickInfoData`









.. py:method:: copy_from_win_id(self, winID: int) -> None
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.copy_from_win_id

    Copy an existing Window's scene into this control.

    :Parameters:

    **winID** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: start_object_editing(self, objEditPath: str) -> None
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.start_object_editing

    Enters into 3D object editing mode.

    :Parameters:

    **objEditPath** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: apply_object_editing(self) -> None
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.apply_object_editing

    Commit changes when in 3D object editing mode.

    :Returns:

        :obj:`~None`

.. py:method:: stop_object_editing(self, canceled: bool) -> None
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.stop_object_editing

    End 3D object editing mode.

    :Parameters:

    **canceled** : :obj:`~bool`

    :Returns:

        :obj:`~None`



.. py:method:: set_mouse_cursor_from_file(self, cursorFileName: str) -> None
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.set_mouse_cursor_from_file

    Set mouse cursor to the selected cursor file.

    :Parameters:

    **cursorFileName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: restore_mouse_cursor(self) -> None
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.restore_mouse_cursor

    Restores mouse cursor back to normal.

    :Returns:

        :obj:`~None`

.. py:method:: set_mouse_cursor_from_handle(self, cursorHandle: int) -> None
    :canonical: ansys.stk.core.stkx.IUiAxGraphics3DCntrl.set_mouse_cursor_from_handle

    Set mouse cursor to the passed cursor handle.

    :Parameters:

    **cursorHandle** : :obj:`~int`

    :Returns:

        :obj:`~None`















