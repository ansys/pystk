MinificationFilter
==================

.. py:class:: ansys.stk.core.graphics.MinificationFilter

   IntEnum


.. py:currentmodule:: MinificationFilter

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~NEAREST`
              - Use the texel that is closest to the center of the pixel being textured.

            * - :py:attr:`~LINEAR`
              - Use the weighted average of the four (for 2D textures, two for 1D textures) texels that are closest to the center of the pixel being textured.

            * - :py:attr:`~NEAREST_MIP_MAP_NEAREST`
              - Use the mipmap that most closely matches the size of the pixel being textured. Then use the texel from that mipmap that is closest to the center of the pixel being textured.

            * - :py:attr:`~LINEAR_MIP_MAP_NEAREST`
              - Use the mipmap that most closely matches the size of the pixel being textured. Then use the weighted average of the four (for 2D textures, two for 1D textures) texels from that mipmap that are closest to the center of the pixel being textured.

            * - :py:attr:`~NEAREST_MIP_MAP_LINEAR`
              - Use the two mipmaps that most closely match the size of the pixel being textured. Determine the texel that is closest to the center of the pixel being textured in each mipmap. The final texture value is a weighted average of these two texels.

            * - :py:attr:`~LINEAR_MIP_MAP_LINEAR`
              - Use the two mipmaps that most closely match the size of the pixel being textured. Determine the weighted average of the four (for 2D textures, two for 1D textures) texels that are closest to the center of the pixel being textured in each mipmap...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import MinificationFilter


