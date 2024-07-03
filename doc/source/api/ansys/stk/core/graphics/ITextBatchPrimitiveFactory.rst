ITextBatchPrimitiveFactory
==========================

.. py:class:: ansys.stk.core.graphics.ITextBatchPrimitiveFactory

   object
   
   Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

.. py:currentmodule:: ITextBatchPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveFactory.initialize_with_graphics_font`
              - Initialize a marker batch primitive with the specified font. This is equivalent to constructing a text batch with the specified font and a set hint of Frequent.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveFactory.initialize_with_graphics_font_and_set_hint`
              - Initialize a marker batch primitive with the specified font and setHint.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveFactory.initialize_with_graphics_font_and_set_hint_2d`
              - Initialize a text batch primitive with the specified font and setHint, optimized for 2d screen space rendering.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITextBatchPrimitiveFactory



Method detail
-------------

.. py:method:: initialize_with_graphics_font(self, font: IGraphicsFont) -> ITextBatchPrimitive
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveFactory.initialize_with_graphics_font

    Initialize a marker batch primitive with the specified font. This is equivalent to constructing a text batch with the specified font and a set hint of Frequent.

    :Parameters:

    **font** : :obj:`~IGraphicsFont`

    :Returns:

        :obj:`~ITextBatchPrimitive`

.. py:method:: initialize_with_graphics_font_and_set_hint(self, font: IGraphicsFont, setHint: SET_HINT) -> ITextBatchPrimitive
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveFactory.initialize_with_graphics_font_and_set_hint

    Initialize a marker batch primitive with the specified font and setHint.

    :Parameters:

    **font** : :obj:`~IGraphicsFont`
    **setHint** : :obj:`~SET_HINT`

    :Returns:

        :obj:`~ITextBatchPrimitive`

.. py:method:: initialize_with_graphics_font_and_set_hint_2d(self, font: IGraphicsFont, setHint: SET_HINT, renderInScreenSpace: bool) -> ITextBatchPrimitive
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveFactory.initialize_with_graphics_font_and_set_hint_2d

    Initialize a text batch primitive with the specified font and setHint, optimized for 2d screen space rendering.

    :Parameters:

    **font** : :obj:`~IGraphicsFont`
    **setHint** : :obj:`~SET_HINT`
    **renderInScreenSpace** : :obj:`~bool`

    :Returns:

        :obj:`~ITextBatchPrimitive`

