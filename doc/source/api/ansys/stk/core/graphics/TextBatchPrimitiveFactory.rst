TextBatchPrimitiveFactory
=========================

.. py:class:: ansys.stk.core.graphics.TextBatchPrimitiveFactory

   Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

.. py:currentmodule:: TextBatchPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitiveFactory.initialize_with_graphics_font`
              - Initialize a marker batch primitive with the specified font. This is equivalent to constructing a text batch with the specified font and a set hint of Frequent.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitiveFactory.initialize_with_graphics_font_and_set_hint`
              - Initialize a marker batch primitive with the specified font and setHint.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitiveFactory.initialize_with_graphics_font_and_set_hint_2d`
              - Initialize a text batch primitive with the specified font and setHint, optimized for 2d screen space rendering.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TextBatchPrimitiveFactory



Method detail
-------------

.. py:method:: initialize_with_graphics_font(self, font: GraphicsFont) -> TextBatchPrimitive
    :canonical: ansys.stk.core.graphics.TextBatchPrimitiveFactory.initialize_with_graphics_font

    Initialize a marker batch primitive with the specified font. This is equivalent to constructing a text batch with the specified font and a set hint of Frequent.

    :Parameters:

        **font** : :obj:`~GraphicsFont`


    :Returns:

        :obj:`~TextBatchPrimitive`

.. py:method:: initialize_with_graphics_font_and_set_hint(self, font: GraphicsFont, set_hint: SetHint) -> TextBatchPrimitive
    :canonical: ansys.stk.core.graphics.TextBatchPrimitiveFactory.initialize_with_graphics_font_and_set_hint

    Initialize a marker batch primitive with the specified font and setHint.

    :Parameters:

        **font** : :obj:`~GraphicsFont`

        **set_hint** : :obj:`~SetHint`


    :Returns:

        :obj:`~TextBatchPrimitive`

.. py:method:: initialize_with_graphics_font_and_set_hint_2d(self, font: GraphicsFont, set_hint: SetHint, render_in_screen_space: bool) -> TextBatchPrimitive
    :canonical: ansys.stk.core.graphics.TextBatchPrimitiveFactory.initialize_with_graphics_font_and_set_hint_2d

    Initialize a text batch primitive with the specified font and setHint, optimized for 2d screen space rendering.

    :Parameters:

        **font** : :obj:`~GraphicsFont`

        **set_hint** : :obj:`~SetHint`

        **render_in_screen_space** : :obj:`~bool`


    :Returns:

        :obj:`~TextBatchPrimitive`

