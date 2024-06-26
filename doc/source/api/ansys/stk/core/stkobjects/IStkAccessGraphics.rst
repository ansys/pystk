IStkAccessGraphics
==================

.. py:class:: ansys.stk.core.stkobjects.IStkAccessGraphics

   object
   
   Provide access to the Graphics for Access Computations.

.. py:currentmodule:: IStkAccessGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessGraphics.inherit`
              - Specifies whether the Access graphics inherit from the Scenario. Otherwise they can be set locally for this object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessGraphics.line_visible`
              - Specifies whether a line appears between objects during access periods in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessGraphics.animate_graphics_2d`
              - Specifies whether an Animate Highlight appears in the 2D Graphics window during access periods. The Animate Highlight is a box drawn around each object participating in the access.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessGraphics.static_graphics_2d`
              - Specifies whether a Static Highlight appears in the 2D Graphics window. The Static Highlight is a thick line overlaying portions of a vehicle's ground track during access periods.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessGraphics.line_width`
              - Line width of lines between objects during access periods in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessGraphics.line_style`
              - Line style of lines between objects during access periods in the 2D and 3D Graphics windows.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkAccessGraphics


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.IStkAccessGraphics.inherit
    :type: bool

    Specifies whether the Access graphics inherit from the Scenario. Otherwise they can be set locally for this object.

.. py:property:: line_visible
    :canonical: ansys.stk.core.stkobjects.IStkAccessGraphics.line_visible
    :type: bool

    Specifies whether a line appears between objects during access periods in the 2D and 3D Graphics windows.

.. py:property:: animate_graphics_2d
    :canonical: ansys.stk.core.stkobjects.IStkAccessGraphics.animate_graphics_2d
    :type: bool

    Specifies whether an Animate Highlight appears in the 2D Graphics window during access periods. The Animate Highlight is a box drawn around each object participating in the access.

.. py:property:: static_graphics_2d
    :canonical: ansys.stk.core.stkobjects.IStkAccessGraphics.static_graphics_2d
    :type: bool

    Specifies whether a Static Highlight appears in the 2D Graphics window. The Static Highlight is a thick line overlaying portions of a vehicle's ground track during access periods.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IStkAccessGraphics.line_width
    :type: int

    Line width of lines between objects during access periods in the 2D and 3D Graphics windows.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.IStkAccessGraphics.line_style
    :type: str

    Line style of lines between objects during access periods in the 2D and 3D Graphics windows.


