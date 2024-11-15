TextureFilter2DFactory
======================

.. py:class:: ansys.stk.core.graphics.TextureFilter2DFactory

   Create texture filters.

.. py:currentmodule:: TextureFilter2DFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2DFactory.initialize`
              - Create a texture filter using the specified minification/magnification options and texture wrap.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2DFactory.initialize_with_texture_wrap`
              - Create a texture filter using the specified texture wrap.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2DFactory.initialize_with_minification_and_magnification`
              - Create a texture filter using the specified minification/magnification options.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2DFactory.nearest_clamp_to_edge`
              - Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: ClampToEdge, WrapT: ClampToEdge.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2DFactory.nearest_repeat`
              - Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: Repeat, WrapT: Repeat.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2DFactory.linear_clamp_to_edge`
              - Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: ClampToEdge, WrapT: ClampToEdge.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2DFactory.linear_repeat`
              - Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: Repeat, WrapT: Repeat.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TextureFilter2DFactory


Property detail
---------------

.. py:property:: nearest_clamp_to_edge
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.nearest_clamp_to_edge
    :type: TextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: ClampToEdge, WrapT: ClampToEdge.

.. py:property:: nearest_repeat
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.nearest_repeat
    :type: TextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: Repeat, WrapT: Repeat.

.. py:property:: linear_clamp_to_edge
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.linear_clamp_to_edge
    :type: TextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: ClampToEdge, WrapT: ClampToEdge.

.. py:property:: linear_repeat
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.linear_repeat
    :type: TextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: Repeat, WrapT: Repeat.


Method detail
-------------





.. py:method:: initialize(self, minification_filter: MINIFICATION_FILTER, magnification_filter: MAGNIFICATION_FILTER, wrap_s: TEXTURE_WRAP, wrap_t: TEXTURE_WRAP) -> TextureFilter2D
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.initialize

    Create a texture filter using the specified minification/magnification options and texture wrap.

    :Parameters:

    **minification_filter** : :obj:`~MINIFICATION_FILTER`
    **magnification_filter** : :obj:`~MAGNIFICATION_FILTER`
    **wrap_s** : :obj:`~TEXTURE_WRAP`
    **wrap_t** : :obj:`~TEXTURE_WRAP`

    :Returns:

        :obj:`~TextureFilter2D`

.. py:method:: initialize_with_texture_wrap(self, wrap_s: TEXTURE_WRAP, wrap_t: TEXTURE_WRAP) -> TextureFilter2D
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.initialize_with_texture_wrap

    Create a texture filter using the specified texture wrap.

    :Parameters:

    **wrap_s** : :obj:`~TEXTURE_WRAP`
    **wrap_t** : :obj:`~TEXTURE_WRAP`

    :Returns:

        :obj:`~TextureFilter2D`

.. py:method:: initialize_with_minification_and_magnification(self, minification_filter: MINIFICATION_FILTER, magnification_filter: MAGNIFICATION_FILTER) -> TextureFilter2D
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.initialize_with_minification_and_magnification

    Create a texture filter using the specified minification/magnification options.

    :Parameters:

    **minification_filter** : :obj:`~MINIFICATION_FILTER`
    **magnification_filter** : :obj:`~MAGNIFICATION_FILTER`

    :Returns:

        :obj:`~TextureFilter2D`

