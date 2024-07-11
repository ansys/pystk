IGraphicsFontFactory
====================

.. py:class:: ansys.stk.core.graphics.IGraphicsFontFactory

   object
   
   A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

.. py:currentmodule:: IGraphicsFontFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IGraphicsFontFactory.initialize_with_name_size_font_style_outline`
              - Initialize a graphics font with the given arguments.
            * - :py:attr:`~ansys.stk.core.graphics.IGraphicsFontFactory.initialize_with_name_size`
              - Initialize a graphics font with the typeface name and size.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGraphicsFontFactory



Method detail
-------------

.. py:method:: initialize_with_name_size_font_style_outline(self, name: str, size: int, fontStyle: FONT_STYLE, outline: bool) -> IGraphicsFont
    :canonical: ansys.stk.core.graphics.IGraphicsFontFactory.initialize_with_name_size_font_style_outline

    Initialize a graphics font with the given arguments.

    :Parameters:

    **name** : :obj:`~str`
    **size** : :obj:`~int`
    **fontStyle** : :obj:`~FONT_STYLE`
    **outline** : :obj:`~bool`

    :Returns:

        :obj:`~IGraphicsFont`

.. py:method:: initialize_with_name_size(self, name: str, size: int) -> IGraphicsFont
    :canonical: ansys.stk.core.graphics.IGraphicsFontFactory.initialize_with_name_size

    Initialize a graphics font with the typeface name and size.

    :Parameters:

    **name** : :obj:`~str`
    **size** : :obj:`~int`

    :Returns:

        :obj:`~IGraphicsFont`

