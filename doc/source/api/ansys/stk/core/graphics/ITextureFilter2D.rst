ITextureFilter2D
================

.. py:class:: ansys.stk.core.graphics.ITextureFilter2D

   object
   
   A texture filter.

.. py:currentmodule:: ITextureFilter2D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2D.minification_filter`
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2D.magnification_filter`
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2D.wrap_s`
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2D.wrap_t`
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2D.nearest_clamp_to_edge`
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2D.nearest_repeat`
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2D.linear_clamp_to_edge`
            * - :py:attr:`~ansys.stk.core.graphics.ITextureFilter2D.linear_repeat`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITextureFilter2D


Property detail
---------------

.. py:property:: minification_filter
    :canonical: ansys.stk.core.graphics.ITextureFilter2D.minification_filter
    :type: MINIFICATION_FILTER

    Gets the minification filter used when the pixel being textured maps to an area less than or equal to one texel.

.. py:property:: magnification_filter
    :canonical: ansys.stk.core.graphics.ITextureFilter2D.magnification_filter
    :type: MAGNIFICATION_FILTER

    Gets the magnification filter used when the pixel being textured maps to an area greater than one texel.

.. py:property:: wrap_s
    :canonical: ansys.stk.core.graphics.ITextureFilter2D.wrap_s
    :type: TEXTURE_WRAP

    Gets the texture wrap for the s direction.

.. py:property:: wrap_t
    :canonical: ansys.stk.core.graphics.ITextureFilter2D.wrap_t
    :type: TEXTURE_WRAP

    Gets the texture wrap for the t direction.

.. py:property:: nearest_clamp_to_edge
    :canonical: ansys.stk.core.graphics.ITextureFilter2D.nearest_clamp_to_edge
    :type: ITextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: ClampToEdge, WrapT: ClampToEdge.

.. py:property:: nearest_repeat
    :canonical: ansys.stk.core.graphics.ITextureFilter2D.nearest_repeat
    :type: ITextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: Repeat, WrapT: Repeat.

.. py:property:: linear_clamp_to_edge
    :canonical: ansys.stk.core.graphics.ITextureFilter2D.linear_clamp_to_edge
    :type: ITextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: ClampToEdge, WrapT: ClampToEdge.

.. py:property:: linear_repeat
    :canonical: ansys.stk.core.graphics.ITextureFilter2D.linear_repeat
    :type: ITextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: Repeat, WrapT: Repeat.


