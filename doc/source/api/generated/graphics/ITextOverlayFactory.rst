ITextOverlayFactory
===================

.. py:class:: ITextOverlayFactory

   object
   
   A rectangular overlay that contains text.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize the overlay with a position of (0, 0), a width of 100 pixels, and a height of 50 pixels.
            * - :py:meth:`~initialize_with_xy_width_height`
              - Initialize the overlay with the specified x position, y position, width, and height, all specified in pixels.
            * - :py:meth:`~initialize_with_position_size`
              - Initialize the overlay with the specified position and size.
            * - :py:meth:`~initialize_with_width_height_units`
              - Initialize the overlay with the specified position and size.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITextOverlayFactory



Method detail
-------------

.. py:method:: initialize(self, font:"IGraphicsFont") -> "ITextOverlay"

    Initialize the overlay with a position of (0, 0), a width of 100 pixels, and a height of 50 pixels.

    :Parameters:

    **font** : :obj:`~"IGraphicsFont"`

    :Returns:

        :obj:`~"ITextOverlay"`

.. py:method:: initialize_with_xy_width_height(self, font:"IGraphicsFont", xPixels:float, yPixels:float, widthPixels:float, heightPixels:float) -> "ITextOverlay"

    Initialize the overlay with the specified x position, y position, width, and height, all specified in pixels.

    :Parameters:

    **font** : :obj:`~"IGraphicsFont"`
    **xPixels** : :obj:`~float`
    **yPixels** : :obj:`~float`
    **widthPixels** : :obj:`~float`
    **heightPixels** : :obj:`~float`

    :Returns:

        :obj:`~"ITextOverlay"`

.. py:method:: initialize_with_position_size(self, font:"IGraphicsFont", position:list, size:list) -> "ITextOverlay"

    Initialize the overlay with the specified position and size.

    :Parameters:

    **font** : :obj:`~"IGraphicsFont"`
    **position** : :obj:`~list`
    **size** : :obj:`~list`

    :Returns:

        :obj:`~"ITextOverlay"`

.. py:method:: initialize_with_width_height_units(self, font:"IGraphicsFont", width:float, widthUnit:"SCREEN_OVERLAY_UNIT", height:float, heightUnit:"SCREEN_OVERLAY_UNIT") -> "ITextOverlay"

    Initialize the overlay with the specified position and size.

    :Parameters:

    **font** : :obj:`~"IGraphicsFont"`
    **width** : :obj:`~float`
    **widthUnit** : :obj:`~"SCREEN_OVERLAY_UNIT"`
    **height** : :obj:`~float`
    **heightUnit** : :obj:`~"SCREEN_OVERLAY_UNIT"`

    :Returns:

        :obj:`~"ITextOverlay"`

