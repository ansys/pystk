GraphicsFontFactory
===================

.. py:class:: ansys.stk.core.graphics.GraphicsFontFactory

   A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

.. py:currentmodule:: GraphicsFontFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.GraphicsFontFactory.initialize_with_name_size_font_style_outline`
              - Initialize a graphics font with the given arguments.
            * - :py:attr:`~ansys.stk.core.graphics.GraphicsFontFactory.initialize_with_name_size`
              - Initialize a graphics font with the typeface name and size.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import GraphicsFontFactory



Method detail
-------------

.. py:method:: initialize_with_name_size_font_style_outline(self, name: str, size: int, font_style: FontStyle, outline: bool) -> GraphicsFont
    :canonical: ansys.stk.core.graphics.GraphicsFontFactory.initialize_with_name_size_font_style_outline

    Initialize a graphics font with the given arguments.

    :Parameters:

        **name** : :obj:`~str`

        **size** : :obj:`~int`

        **font_style** : :obj:`~FontStyle`

        **outline** : :obj:`~bool`


    :Returns:

        :obj:`~GraphicsFont`

.. py:method:: initialize_with_name_size(self, name: str, size: int) -> GraphicsFont
    :canonical: ansys.stk.core.graphics.GraphicsFontFactory.initialize_with_name_size

    Initialize a graphics font with the typeface name and size.

    :Parameters:

        **name** : :obj:`~str`

        **size** : :obj:`~int`


    :Returns:

        :obj:`~GraphicsFont`

