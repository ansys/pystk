Graphics3DDataDisplayElement
============================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement

   Class defining 3D Graphics data display element.

.. py:currentmodule:: Graphics3DDataDisplayElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.add_to_all_windows`
              - Add the data display to all 3D windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.add_to_window`
              - Add the data display to a 3D window.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.is_displayed_in_window`
              - Opt whether to show the data display in the selected location.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.remove_from_window`
              - Remove the data display from a 3D window.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.available_windows`
              - Get the available 3D windows for the data display.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_border_color`
              - Get or set the color of the border surrounding the data display background.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_color`
              - Get or set the color of the data display background.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_height`
              - Get or set the height of the data display background. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_texture_filename`
              - Get or set the filename of the background texture.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_translucency`
              - Get or set the translucency of the background between 0 and 1 inclusive.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_width`
              - Get or set the width of the data display background. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.font_color`
              - Font color of the data display.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.font_size`
              - Font size of the data display.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.format`
              - Font format of the data display.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.location`
              - Get or set the location where the data display is to appear: 3D window, data display area, or offset from the selected object.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.name`
              - Name of data display element.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.show_graphics`
              - Opt whether to show the data display element.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.show_name`
              - Opt whether to show an objects name in the data display title.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.title`
              - Opt whether to show the title of the data display.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.title_text`
              - Get or set the title of the data display.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.transparent_background`
              - Opt whether to make the background transparent.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.use_automatic_size_height`
              - Opt whether to allow automatic resizing of data display height.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.use_automatic_size_width`
              - Opt whether to allow automatic resizing of data display width.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.use_background`
              - Opt whether to use a background with the data display.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.use_background_border`
              - Opt whether to use a background border with the data display.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.use_background_texture`
              - Opt whether to use a background texture with the data display.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.x`
              - Amount of X offset from the origin. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.x_origin`
              - Get or set the horizontal point of origin for the marker (left, center or right).
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.y`
              - Amount of Y offset from the origin. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.y_origin`
              - Get or set the vertical point of origin for the marker (top, center or bottom.).



Examples
--------

Add a Data Display to the 3D Window

.. code-block:: python

    # Satellite satellite: Satellite object
    # Remove all data displays so you can easily pick one that may already be in
    # the list
    satellite.graphics_3d.data_display.remove_all()
    # Add LLA data display and change size/title
    datadisplay = satellite.graphics_3d.data_display.add("LLA Position")
    datadisplay.show_graphics = True
    datadisplay.font_size = Graphics3DFontSize.MEDIUM
    datadisplay.title_text = "My Data Display"
    datadisplay.show_name = False


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DDataDisplayElement


Property detail
---------------

.. py:property:: available_windows
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.available_windows
    :type: list

    Get the available 3D windows for the data display.

.. py:property:: background_border_color
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_border_color
    :type: Color

    Get or set the color of the border surrounding the data display background.

.. py:property:: background_color
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_color
    :type: Color

    Get or set the color of the data display background.

.. py:property:: background_height
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_height
    :type: int

    Get or set the height of the data display background. Dimensionless.

.. py:property:: background_texture_filename
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_texture_filename
    :type: str

    Get or set the filename of the background texture.

.. py:property:: background_translucency
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_translucency
    :type: float

    Get or set the translucency of the background between 0 and 1 inclusive.

.. py:property:: background_width
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.background_width
    :type: int

    Get or set the width of the data display background. Dimensionless.

.. py:property:: font_color
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.font_color
    :type: Color

    Font color of the data display.

.. py:property:: font_size
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.font_size
    :type: Graphics3DFontSize

    Font size of the data display.

.. py:property:: format
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.format
    :type: Graphics3DFormat

    Font format of the data display.

.. py:property:: location
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.location
    :type: Graphics3DLocation

    Get or set the location where the data display is to appear: 3D window, data display area, or offset from the selected object.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.name
    :type: str

    Name of data display element.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.show_graphics
    :type: bool

    Opt whether to show the data display element.

.. py:property:: show_name
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.show_name
    :type: bool

    Opt whether to show an objects name in the data display title.

.. py:property:: title
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.title
    :type: bool

    Opt whether to show the title of the data display.

.. py:property:: title_text
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.title_text
    :type: str

    Get or set the title of the data display.

.. py:property:: transparent_background
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.transparent_background
    :type: bool

    Opt whether to make the background transparent.

.. py:property:: use_automatic_size_height
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.use_automatic_size_height
    :type: bool

    Opt whether to allow automatic resizing of data display height.

.. py:property:: use_automatic_size_width
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.use_automatic_size_width
    :type: bool

    Opt whether to allow automatic resizing of data display width.

.. py:property:: use_background
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.use_background
    :type: bool

    Opt whether to use a background with the data display.

.. py:property:: use_background_border
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.use_background_border
    :type: bool

    Opt whether to use a background border with the data display.

.. py:property:: use_background_texture
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.use_background_texture
    :type: bool

    Opt whether to use a background texture with the data display.

.. py:property:: x
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.x
    :type: int

    Amount of X offset from the origin. Dimensionless.

.. py:property:: x_origin
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.x_origin
    :type: Graphics3DXOrigin

    Get or set the horizontal point of origin for the marker (left, center or right).

.. py:property:: y
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.y
    :type: int

    Amount of Y offset from the origin. Dimensionless.

.. py:property:: y_origin
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.y_origin
    :type: Graphics3DYOrigin

    Get or set the vertical point of origin for the marker (top, center or bottom.).


Method detail
-------------

.. py:method:: add_to_all_windows(self) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.add_to_all_windows

    Add the data display to all 3D windows.

    :Returns:

        :obj:`~None`

.. py:method:: add_to_window(self, title: str) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.add_to_window

    Add the data display to a 3D window.

    :Parameters:

        **title** : :obj:`~str`


    :Returns:

        :obj:`~None`




















.. py:method:: is_displayed_in_window(self, title: str) -> bool
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.is_displayed_in_window

    Opt whether to show the data display in the selected location.

    :Parameters:

        **title** : :obj:`~str`


    :Returns:

        :obj:`~bool`








.. py:method:: remove_from_window(self, title: str) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayElement.remove_from_window

    Remove the data display from a 3D window.

    :Parameters:

        **title** : :obj:`~str`


    :Returns:

        :obj:`~None`

























