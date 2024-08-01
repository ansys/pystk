GraphicsFont
============

.. py:class:: ansys.stk.core.graphics.GraphicsFont

   A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

.. py:currentmodule:: GraphicsFont

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.GraphicsFont.name`
              - Gets the typeface name of the font.
            * - :py:attr:`~ansys.stk.core.graphics.GraphicsFont.size`
              - Gets the size of the font.
            * - :py:attr:`~ansys.stk.core.graphics.GraphicsFont.bold`
              - Gets a value that indicates whether this font is bold.
            * - :py:attr:`~ansys.stk.core.graphics.GraphicsFont.italic`
              - Gets a value that indicates whether this font is italic.
            * - :py:attr:`~ansys.stk.core.graphics.GraphicsFont.underline`
              - Gets a value that indicates whether this font is underlined.
            * - :py:attr:`~ansys.stk.core.graphics.GraphicsFont.strikeout`
              - Gets a value that indicates whether this font has a horizontal line through its characters.
            * - :py:attr:`~ansys.stk.core.graphics.GraphicsFont.outline`
              - Gets a value that indicates whether this font has an outline around its characters.
            * - :py:attr:`~ansys.stk.core.graphics.GraphicsFont.style`
              - Gets the font style enumeration that contains the style for this font. This does not include the outline property.
            * - :py:attr:`~ansys.stk.core.graphics.GraphicsFont.antialias`
              - Gets a value that indicates whether this font is antialiased.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import GraphicsFont


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.graphics.GraphicsFont.name
    :type: str

    Gets the typeface name of the font.

.. py:property:: size
    :canonical: ansys.stk.core.graphics.GraphicsFont.size
    :type: int

    Gets the size of the font.

.. py:property:: bold
    :canonical: ansys.stk.core.graphics.GraphicsFont.bold
    :type: bool

    Gets a value that indicates whether this font is bold.

.. py:property:: italic
    :canonical: ansys.stk.core.graphics.GraphicsFont.italic
    :type: bool

    Gets a value that indicates whether this font is italic.

.. py:property:: underline
    :canonical: ansys.stk.core.graphics.GraphicsFont.underline
    :type: bool

    Gets a value that indicates whether this font is underlined.

.. py:property:: strikeout
    :canonical: ansys.stk.core.graphics.GraphicsFont.strikeout
    :type: bool

    Gets a value that indicates whether this font has a horizontal line through its characters.

.. py:property:: outline
    :canonical: ansys.stk.core.graphics.GraphicsFont.outline
    :type: bool

    Gets a value that indicates whether this font has an outline around its characters.

.. py:property:: style
    :canonical: ansys.stk.core.graphics.GraphicsFont.style
    :type: FONT_STYLE

    Gets the font style enumeration that contains the style for this font. This does not include the outline property.

.. py:property:: antialias
    :canonical: ansys.stk.core.graphics.GraphicsFont.antialias
    :type: bool

    Gets a value that indicates whether this font is antialiased.


