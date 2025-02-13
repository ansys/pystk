AccessGraphics
==============

.. py:class:: ansys.stk.core.stkobjects.AccessGraphics

   Class defining 2D Graphics for Access.

.. py:currentmodule:: AccessGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessGraphics.inherit`
              - Specify whether the Access graphics inherit from the Scenario. Otherwise they can be set locally for this object.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessGraphics.show_line`
              - Specify whether a line appears between objects during access periods in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessGraphics.show_animation_highlight_graphics_2d`
              - Specify whether an Animate Highlight appears in the 2D Graphics window during access periods. The Animate Highlight is a box drawn around each object participating in the access.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessGraphics.static_graphics_2d`
              - Specify whether a Static Highlight appears in the 2D Graphics window. The Static Highlight is a thick line overlaying portions of a vehicle's ground track during access periods.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessGraphics.line_width`
              - Line width of lines between objects during access periods in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessGraphics.line_style`
              - Line style of lines between objects during access periods in the 2D and 3D Graphics windows.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessGraphics


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.AccessGraphics.inherit
    :type: bool

    Specify whether the Access graphics inherit from the Scenario. Otherwise they can be set locally for this object.

.. py:property:: show_line
    :canonical: ansys.stk.core.stkobjects.AccessGraphics.show_line
    :type: bool

    Specify whether a line appears between objects during access periods in the 2D and 3D Graphics windows.

.. py:property:: show_animation_highlight_graphics_2d
    :canonical: ansys.stk.core.stkobjects.AccessGraphics.show_animation_highlight_graphics_2d
    :type: bool

    Specify whether an Animate Highlight appears in the 2D Graphics window during access periods. The Animate Highlight is a box drawn around each object participating in the access.

.. py:property:: static_graphics_2d
    :canonical: ansys.stk.core.stkobjects.AccessGraphics.static_graphics_2d
    :type: bool

    Specify whether a Static Highlight appears in the 2D Graphics window. The Static Highlight is a thick line overlaying portions of a vehicle's ground track during access periods.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.AccessGraphics.line_width
    :type: int

    Line width of lines between objects during access periods in the 2D and 3D Graphics windows.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.AccessGraphics.line_style
    :type: str

    Line style of lines between objects during access periods in the 2D and 3D Graphics windows.


