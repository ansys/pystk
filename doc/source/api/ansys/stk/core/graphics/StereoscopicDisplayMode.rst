StereoscopicDisplayMode
=======================

.. py:class:: ansys.stk.core.graphics.StereoscopicDisplayMode

   IntEnum


.. py:currentmodule:: StereoscopicDisplayMode

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~OFF`
              - No stereoscopic.

            * - :py:attr:`~QUAD_BUFFER`
              - OpenGL Quad-buffer stereoscopic.

            * - :py:attr:`~ANAGLYPH`
              - Anaglyph or two-color stereoscopic.

            * - :py:attr:`~LEFT_EYE`
              - Left eye view of the stereoscopic scene.

            * - :py:attr:`~RIGHT_EYE`
              - Right eye view of the stereoscopic scene.

            * - :py:attr:`~SIDE_BY_SIDE`
              - Side-by-side stereoscopic. Left and right eye views are rendered next to each other in the same window.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import StereoscopicDisplayMode


