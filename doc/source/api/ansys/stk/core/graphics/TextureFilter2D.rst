TextureFilter2D
===============

.. py:class:: ansys.stk.core.graphics.TextureFilter2D

   A texture filter.

.. py:currentmodule:: TextureFilter2D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2D.minification_filter`
              - Gets the minification filter used when the pixel being textured maps to an area less than or equal to one texel.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2D.magnification_filter`
              - Gets the magnification filter used when the pixel being textured maps to an area greater than one texel.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2D.wrap_s`
              - Gets the texture wrap for the s direction.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2D.wrap_t`
              - Gets the texture wrap for the t direction.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2D.nearest_clamp_to_edge`
              - Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: ClampToEdge, WrapT: ClampToEdge.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2D.nearest_repeat`
              - Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: Repeat, WrapT: Repeat.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2D.linear_clamp_to_edge`
              - Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: ClampToEdge, WrapT: ClampToEdge.
            * - :py:attr:`~ansys.stk.core.graphics.TextureFilter2D.linear_repeat`
              - Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: Repeat, WrapT: Repeat.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TextureFilter2D


Property detail
---------------

.. py:property:: minification_filter
    :canonical: ansys.stk.core.graphics.TextureFilter2D.minification_filter
    :type: MinificationFilter

    Gets the minification filter used when the pixel being textured maps to an area less than or equal to one texel.

.. py:property:: magnification_filter
    :canonical: ansys.stk.core.graphics.TextureFilter2D.magnification_filter
    :type: MagnificationFilter

    Gets the magnification filter used when the pixel being textured maps to an area greater than one texel.

.. py:property:: wrap_s
    :canonical: ansys.stk.core.graphics.TextureFilter2D.wrap_s
    :type: TextureWrap

    Gets the texture wrap for the s direction.

.. py:property:: wrap_t
    :canonical: ansys.stk.core.graphics.TextureFilter2D.wrap_t
    :type: TextureWrap

    Gets the texture wrap for the t direction.

.. py:property:: nearest_clamp_to_edge
    :canonical: ansys.stk.core.graphics.TextureFilter2D.nearest_clamp_to_edge
    :type: TextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: ClampToEdge, WrapT: ClampToEdge.

.. py:property:: nearest_repeat
    :canonical: ansys.stk.core.graphics.TextureFilter2D.nearest_repeat
    :type: TextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Nearest, MagnificationFilter: Nearest, WrapS: Repeat, WrapT: Repeat.

.. py:property:: linear_clamp_to_edge
    :canonical: ansys.stk.core.graphics.TextureFilter2D.linear_clamp_to_edge
    :type: TextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: ClampToEdge, WrapT: ClampToEdge.

.. py:property:: linear_repeat
    :canonical: ansys.stk.core.graphics.TextureFilter2D.linear_repeat
    :type: TextureFilter2D

    Gets a texture filter with the following properties: MinificationFilter: Linear, MagnificationFilter: Linear, WrapS: Repeat, WrapT: Repeat.


