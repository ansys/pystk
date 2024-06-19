IGraphics3DDataDisplayElement
=============================

.. py:class:: IGraphics3DDataDisplayElement

   object
   
   Interface for 3D Graphics window data display element.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_displayed_in_window`
              - Opt whether to show the data display in the selected location.
            * - :py:meth:`~add_to_window`
              - Add the data display to a 3D window.
            * - :py:meth:`~remove_from_window`
              - Remove the data display from a 3D window.
            * - :py:meth:`~add_to_all_windows`
              - Add the data display to all 3D windows.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~is_visible`
            * - :py:meth:`~location`
            * - :py:meth:`~x_origin`
            * - :py:meth:`~x`
            * - :py:meth:`~y_origin`
            * - :py:meth:`~y`
            * - :py:meth:`~title`
            * - :py:meth:`~font_size`
            * - :py:meth:`~font_color`
            * - :py:meth:`~format`
            * - :py:meth:`~use_background`
            * - :py:meth:`~transparent_bg`
            * - :py:meth:`~bg_width`
            * - :py:meth:`~bg_height`
            * - :py:meth:`~bg_color`
            * - :py:meth:`~available_windows`
            * - :py:meth:`~title_text`
            * - :py:meth:`~background_translucency`
            * - :py:meth:`~use_background_texture`
            * - :py:meth:`~background_texture_filename`
            * - :py:meth:`~use_background_border`
            * - :py:meth:`~background_border_color`
            * - :py:meth:`~use_auto_size_width`
            * - :py:meth:`~use_auto_size_height`
            * - :py:meth:`~is_show_name_enabled`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DDataDisplayElement


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.name
    :type: str

    Name of data display element.

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.is_visible
    :type: bool

    Opt whether to show the data display element.

.. py:property:: location
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.location
    :type: GRAPHICS_3D_LOCATION

    Gets or sets the location where the data display is to appear: 3D window, data display area, or offset from the selected object.

.. py:property:: x_origin
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.x_origin
    :type: GRAPHICS_3D_X_ORIGIN

    Gets or sets the horizontal point of origin for the marker (left, center or right).

.. py:property:: x
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.x
    :type: int

    Amount of X offset from the origin. Dimensionless.

.. py:property:: y_origin
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.y_origin
    :type: GRAPHICS_3D_Y_ORIGIN

    Gets or sets the vertical point of origin for the marker (top, center or bottom.).

.. py:property:: y
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.y
    :type: int

    Amount of Y offset from the origin. Dimensionless.

.. py:property:: title
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.title
    :type: bool

    Opt whether to show the title of the data display.

.. py:property:: font_size
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.font_size
    :type: GRAPHICS_3D_FONT_SIZE

    Font size of the data display.

.. py:property:: font_color
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.font_color
    :type: agcolor.Color

    Font color of the data display.

.. py:property:: format
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.format
    :type: GRAPHICS_3D_FORMAT

    Font format of the data display.

.. py:property:: use_background
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.use_background
    :type: bool

    Opt whether to use a background with the data display.

.. py:property:: transparent_bg
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.transparent_bg
    :type: bool

    Opt whether to make the background transparent.

.. py:property:: bg_width
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.bg_width
    :type: int

    Gets or sets the width of the data display background. Dimensionless.

.. py:property:: bg_height
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.bg_height
    :type: int

    Gets or sets the height of the data display background. Dimensionless.

.. py:property:: bg_color
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.bg_color
    :type: agcolor.Color

    Gets or sets the color of the data display background.

.. py:property:: available_windows
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.available_windows
    :type: list

    Get the available 3D windows for the data display.

.. py:property:: title_text
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.title_text
    :type: str

    Gets or sets the title of the data display.

.. py:property:: background_translucency
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.background_translucency
    :type: float

    Gets or sets the translucency of the background between 0 and 1 inclusive.

.. py:property:: use_background_texture
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.use_background_texture
    :type: bool

    Opt whether to use a background texture with the data display.

.. py:property:: background_texture_filename
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.background_texture_filename
    :type: str

    Gets or sets the filename of the background texture.

.. py:property:: use_background_border
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.use_background_border
    :type: bool

    Opt whether to use a background border with the data display.

.. py:property:: background_border_color
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.background_border_color
    :type: agcolor.Color

    Gets or sets the color of the border surrounding the data display background.

.. py:property:: use_auto_size_width
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.use_auto_size_width
    :type: bool

    Opt whether to allow automatic resizing of data display width.

.. py:property:: use_auto_size_height
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.use_auto_size_height
    :type: bool

    Opt whether to allow automatic resizing of data display height.

.. py:property:: is_show_name_enabled
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.is_show_name_enabled
    :type: bool

    Opt whether to show an objects name in the data display title.


Method detail
-------------




.. py:method:: is_displayed_in_window(self, title: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.is_displayed_in_window

    Opt whether to show the data display in the selected location.

    :Parameters:

    **title** : :obj:`~str`

    :Returns:

        :obj:`~bool`






























.. py:method:: add_to_window(self, title: str) -> None
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.add_to_window

    Add the data display to a 3D window.

    :Parameters:

    **title** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_from_window(self, title: str) -> None
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.remove_from_window

    Remove the data display from a 3D window.

    :Parameters:

    **title** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: add_to_all_windows(self) -> None
    :canonical: ansys.stk.core.stkobjects.IGraphics3DDataDisplayElement.add_to_all_windows

    Add the data display to all 3D windows.

    :Returns:

        :obj:`~None`



















