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
              - Get a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: ClampToEdge, WrapT: ClampToEdge.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2DFactory.nearest_repeat`
              - Get a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: Repeat, WrapT: Repeat.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2DFactory.linear_clamp_to_edge`
              - Get a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: ClampToEdge, WrapT: ClampToEdge.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2DFactory.linear_repeat`
              - Get a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: Repeat, WrapT: Repeat.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TextureFilter2DFactory


Property detail
---------------

.. py:property:: nearest_clamp_to_edge
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.nearest_clamp_to_edge
    :type: TextureFilter2D

    Get a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: ClampToEdge, WrapT: ClampToEdge.

.. py:property:: nearest_repeat
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.nearest_repeat
    :type: TextureFilter2D

    Get a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: Repeat, WrapT: Repeat.

.. py:property:: linear_clamp_to_edge
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.linear_clamp_to_edge
    :type: TextureFilter2D

    Get a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: ClampToEdge, WrapT: ClampToEdge.

.. py:property:: linear_repeat
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.linear_repeat
    :type: TextureFilter2D

    Get a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: Repeat, WrapT: Repeat.


Method detail
-------------





.. py:method:: initialize(self, minification_filter: MinificationFilter, magnification_filter: MagnificationFilter, wrap_s: TextureWrap, wrap_t: TextureWrap) -> TextureFilter2D
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.initialize

    Create a texture filter using the specified minification/magnification options and texture wrap.

    :Parameters:

    **minification_filter** : :obj:`~MinificationFilter`
    **magnification_filter** : :obj:`~MagnificationFilter`
    **wrap_s** : :obj:`~TextureWrap`
    **wrap_t** : :obj:`~TextureWrap`

    :Returns:

        :obj:`~TextureFilter2D`

.. py:method:: initialize_with_texture_wrap(self, wrap_s: TextureWrap, wrap_t: TextureWrap) -> TextureFilter2D
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.initialize_with_texture_wrap

    Create a texture filter using the specified texture wrap.

    :Parameters:

    **wrap_s** : :obj:`~TextureWrap`
    **wrap_t** : :obj:`~TextureWrap`

    :Returns:

        :obj:`~TextureFilter2D`

.. py:method:: initialize_with_minification_and_magnification(self, minification_filter: MinificationFilter, magnification_filter: MagnificationFilter) -> TextureFilter2D
    :canonical: ansys.stk.core.graphics.TextureFilter2DFactory.initialize_with_minification_and_magnification

    Create a texture filter using the specified minification/magnification options.

    :Parameters:

    **minification_filter** : :obj:`~MinificationFilter`
    **magnification_filter** : :obj:`~MagnificationFilter`

    :Returns:

        :obj:`~TextureFilter2D`

