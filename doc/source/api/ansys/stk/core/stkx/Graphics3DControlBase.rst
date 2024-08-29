Graphics3DControlBase
=====================

.. py:class:: ansys.stk.core.stkx.Graphics3DControlBase

   AGI Globe control.

.. py:currentmodule:: Graphics3DControlBase

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.picture_put_reference`
              - Set a reference to the splash logo graphic to be displayed in the control.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.pick_info`
              - Get detailed information about a mouse pick.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.zoom_in`
              - Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.rubber_band_pick_info`
              - Get detailed information about a rubber-band mouse pick. The values must be within the VO window (0 to width-1 for left and right, 0 to height-1 for top and bottom).
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.copy_from_window_id`
              - Copy an existing Window's scene into this control.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.start_object_editing`
              - Enters into 3D object editing mode.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.apply_object_editing`
              - Commit changes when in 3D object editing mode.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.stop_object_editing`
              - End 3D object editing mode.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.set_mouse_cursor_from_file`
              - Set mouse cursor to the selected cursor file.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.restore_mouse_cursor`
              - Restores mouse cursor back to normal.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.set_mouse_cursor_from_handle`
              - Set mouse cursor to the passed cursor handle.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.Subscribe`
              - """Return an IUiAxGraphics3DCntrlEventHandler that is subscribed to handle events associated with this instance of Graphics3DControlBase."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.back_color`
              - The background color of the control.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.picture`
              - The splash logo graphic to be displayed in the control.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.window_id`
              - Window identifier (for Connect commands).
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.application`
              - Reference to the STK X application object.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.no_logo`
              - If true, the splash logo is not shown.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.ole_drop_mode`
              - How the control handles drop operations.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.vendor_id`
              - This property is deprecated. The identifier of the vendor.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.mouse_mode`
              - Whether this control responds to mouse events.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.draw_elements`
              - Elements to draw on the control.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.ready_state`
              - Returns/sets the background color of the control.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.ppt_preload_mode`
              - Special mode for PowerPoint : if true the VO control window is kept around when switching between slides.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.advanced_pick_mode`
              - If true, sets the advance pick mode.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.is_object_editing`
              - Returns true if in 3D object editing mode.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.in_zoom_mode`
              - Returns true if in zoom in mode.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.show_progress_image`
              - The animated progress image type.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.progress_image_x_offset`
              - The horizontal X offset for animated progress image.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.progress_image_y_offset`
              - The vertical Y offset for animated progress image.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.progress_image_file`
              - The complete image file name/path for animated progress image.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.progress_image_x_origin`
              - The X origin alignment for animated progress image.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.progress_image_y_origin`
              - The Y origin alignment for animated progress image.
            * - :py:attr:`~ansys.stk.core.stkx.Graphics3DControlBase.picture_from_file`
              - Gets or sets the splash logo graphic file to be displayed in the control.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import Graphics3DControlBase


Property detail
---------------

.. py:property:: back_color
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.back_color
    :type: agcolor.Color

    The background color of the control.

.. py:property:: picture
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.picture
    :type: IPictureDisp

    The splash logo graphic to be displayed in the control.

.. py:property:: window_id
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.window_id
    :type: int

    Window identifier (for Connect commands).

.. py:property:: application
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.application
    :type: STKXApplication

    Reference to the STK X application object.

.. py:property:: no_logo
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.no_logo
    :type: bool

    If true, the splash logo is not shown.

.. py:property:: ole_drop_mode
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.ole_drop_mode
    :type: OLE_DROP_MODE

    How the control handles drop operations.

.. py:property:: vendor_id
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.vendor_id
    :type: str

    This property is deprecated. The identifier of the vendor.

.. py:property:: mouse_mode
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.mouse_mode
    :type: MOUSE_MODE

    Whether this control responds to mouse events.

.. py:property:: draw_elements
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.draw_elements
    :type: IDrawElementCollection

    Elements to draw on the control.

.. py:property:: ready_state
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.ready_state
    :type: int

    Returns/sets the background color of the control.

.. py:property:: ppt_preload_mode
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.ppt_preload_mode
    :type: bool

    Special mode for PowerPoint : if true the VO control window is kept around when switching between slides.

.. py:property:: advanced_pick_mode
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.advanced_pick_mode
    :type: bool

    If true, sets the advance pick mode.

.. py:property:: is_object_editing
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.is_object_editing
    :type: bool

    Returns true if in 3D object editing mode.

.. py:property:: in_zoom_mode
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.in_zoom_mode
    :type: bool

    Returns true if in zoom in mode.

.. py:property:: show_progress_image
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.show_progress_image
    :type: SHOW_PROGRESS_IMAGE

    The animated progress image type.

.. py:property:: progress_image_x_offset
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.progress_image_x_offset
    :type: int

    The horizontal X offset for animated progress image.

.. py:property:: progress_image_y_offset
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.progress_image_y_offset
    :type: int

    The vertical Y offset for animated progress image.

.. py:property:: progress_image_file
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.progress_image_file
    :type: str

    The complete image file name/path for animated progress image.

.. py:property:: progress_image_x_origin
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.progress_image_x_origin
    :type: PROGRESS_IMAGE_X_ORIGIN

    The X origin alignment for animated progress image.

.. py:property:: progress_image_y_origin
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.progress_image_y_origin
    :type: PROGRESS_IMAGE_Y_ORIGIN

    The Y origin alignment for animated progress image.

.. py:property:: picture_from_file
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.picture_from_file
    :type: str

    Gets or sets the splash logo graphic file to be displayed in the control.


Method detail
-------------




.. py:method:: picture_put_reference(self, pPicture: IPictureDisp) -> None
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.picture_put_reference

    Set a reference to the splash logo graphic to be displayed in the control.

    :Parameters:

    **pPicture** : :obj:`~IPictureDisp`

    :Returns:

        :obj:`~None`


.. py:method:: pick_info(self, x: int, y: int) -> PickInfoData
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.pick_info

    Get detailed information about a mouse pick.

    :Parameters:

    **x** : :obj:`~int`
    **y** : :obj:`~int`

    :Returns:

        :obj:`~PickInfoData`




.. py:method:: zoom_in(self) -> None
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.zoom_in

    Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom.

    :Returns:

        :obj:`~None`







.. py:method:: rubber_band_pick_info(self, left: int, top: int, right: int, bottom: int) -> RubberBandPickInfoData
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.rubber_band_pick_info

    Get detailed information about a rubber-band mouse pick. The values must be within the VO window (0 to width-1 for left and right, 0 to height-1 for top and bottom).

    :Parameters:

    **left** : :obj:`~int`
    **top** : :obj:`~int`
    **right** : :obj:`~int`
    **bottom** : :obj:`~int`

    :Returns:

        :obj:`~RubberBandPickInfoData`









.. py:method:: copy_from_window_id(self, winID: int) -> None
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.copy_from_window_id

    Copy an existing Window's scene into this control.

    :Parameters:

    **winID** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: start_object_editing(self, objEditPath: str) -> None
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.start_object_editing

    Enters into 3D object editing mode.

    :Parameters:

    **objEditPath** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: apply_object_editing(self) -> None
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.apply_object_editing

    Commit changes when in 3D object editing mode.

    :Returns:

        :obj:`~None`

.. py:method:: stop_object_editing(self, canceled: bool) -> None
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.stop_object_editing

    End 3D object editing mode.

    :Parameters:

    **canceled** : :obj:`~bool`

    :Returns:

        :obj:`~None`



.. py:method:: set_mouse_cursor_from_file(self, cursorFileName: str) -> None
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.set_mouse_cursor_from_file

    Set mouse cursor to the selected cursor file.

    :Parameters:

    **cursorFileName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: restore_mouse_cursor(self) -> None
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.restore_mouse_cursor

    Restores mouse cursor back to normal.

    :Returns:

        :obj:`~None`

.. py:method:: set_mouse_cursor_from_handle(self, cursorHandle: int) -> None
    :canonical: ansys.stk.core.stkx.Graphics3DControlBase.set_mouse_cursor_from_handle

    Set mouse cursor to the passed cursor handle.

    :Parameters:

    **cursorHandle** : :obj:`~int`

    :Returns:

        :obj:`~None`















