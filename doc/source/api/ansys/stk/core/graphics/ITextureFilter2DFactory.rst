ITextureFilter2DFactory
=======================

.. py:class:: ansys.stk.core.graphics.ITextureFilter2DFactory

   object
   
   Create texture filters.

.. py:currentmodule:: ITextureFilter2DFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2DFactory.initialize`
              - Create a texture filter using the specified minification/magnification options and texture wrap.
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2DFactory.initialize_with_texture_wrap`
              - Create a texture filter using the specified texture wrap.
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2DFactory.initialize_with_minification_and_magnification`
              - Create a texture filter using the specified minification/magnification options.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2DFactory.nearest_clamp_to_edge`
              - Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: ClampToEdge, WrapT: ClampToEdge.
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2DFactory.nearest_repeat`
              - Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: Repeat, WrapT: Repeat.
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2DFactory.linear_clamp_to_edge`
              - Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: ClampToEdge, WrapT: ClampToEdge.
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2DFactory.linear_repeat`
              - Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: Repeat, WrapT: Repeat.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITextureFilter2DFactory


Property detail
---------------

.. py:property:: nearest_clamp_to_edge
    :canonical: ansys.stk.core.graphics.ITextureFilter2DFactory.nearest_clamp_to_edge
    :type: ITextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: ClampToEdge, WrapT: ClampToEdge.

.. py:property:: nearest_repeat
    :canonical: ansys.stk.core.graphics.ITextureFilter2DFactory.nearest_repeat
    :type: ITextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: Repeat, WrapT: Repeat.

.. py:property:: linear_clamp_to_edge
    :canonical: ansys.stk.core.graphics.ITextureFilter2DFactory.linear_clamp_to_edge
    :type: ITextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: ClampToEdge, WrapT: ClampToEdge.

.. py:property:: linear_repeat
    :canonical: ansys.stk.core.graphics.ITextureFilter2DFactory.linear_repeat
    :type: ITextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: Repeat, WrapT: Repeat.


Method detail
-------------





.. py:method:: initialize(self, minificationFilter: MINIFICATION_FILTER, magnificationFilter: MAGNIFICATION_FILTER, wrapS: TEXTURE_WRAP, wrapT: TEXTURE_WRAP) -> ITextureFilter2D
    :canonical: ansys.stk.core.graphics.ITextureFilter2DFactory.initialize

    Create a texture filter using the specified minification/magnification options and texture wrap.

    :Parameters:

    **minificationFilter** : :obj:`~MINIFICATION_FILTER`
    **magnificationFilter** : :obj:`~MAGNIFICATION_FILTER`
    **wrapS** : :obj:`~TEXTURE_WRAP`
    **wrapT** : :obj:`~TEXTURE_WRAP`

    :Returns:

        :obj:`~ITextureFilter2D`

.. py:method:: initialize_with_texture_wrap(self, wrapS: TEXTURE_WRAP, wrapT: TEXTURE_WRAP) -> ITextureFilter2D
    :canonical: ansys.stk.core.graphics.ITextureFilter2DFactory.initialize_with_texture_wrap

    Create a texture filter using the specified texture wrap.

    :Parameters:

    **wrapS** : :obj:`~TEXTURE_WRAP`
    **wrapT** : :obj:`~TEXTURE_WRAP`

    :Returns:

        :obj:`~ITextureFilter2D`

.. py:method:: initialize_with_minification_and_magnification(self, minificationFilter: MINIFICATION_FILTER, magnificationFilter: MAGNIFICATION_FILTER) -> ITextureFilter2D
    :canonical: ansys.stk.core.graphics.ITextureFilter2DFactory.initialize_with_minification_and_magnification

    Create a texture filter using the specified minification/magnification options.

    :Parameters:

    **minificationFilter** : :obj:`~MINIFICATION_FILTER`
    **magnificationFilter** : :obj:`~MAGNIFICATION_FILTER`

    :Returns:

        :obj:`~ITextureFilter2D`

