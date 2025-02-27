ScreenOverlayOrigin
===================

.. py:class:: ansys.stk.core.graphics.ScreenOverlayOrigin

   IntEnum


.. py:currentmodule:: ScreenOverlayOrigin

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~BOTTOM_LEFT`
              - When the X and Y position are both set to 0, this value places the bottom, left corner of the overlay in its parent's bottom, left corner. Increasing X values move the overlay to the right and increasing Y values move it up.

            * - :py:attr:`~BOTTOM_CENTER`
              - When the X and Y position are both set to 0, this value places the bottom edge of the overlay at its parent's bottom edge and the center of the overlay is horizontally centered within its parent...

            * - :py:attr:`~BOTTOM_RIGHT`
              - When the X and Y position are both set to 0, this value places the bottom, right corner of the overlay in its parent's bottom, right corner. Increasing X values move the overlay to the left and increasing Y values move it up.

            * - :py:attr:`~CENTER_LEFT`
              - When the X and Y position are both set to 0, this value places the left edge of the overlay at its parent's left edge and the center of the overlay is vertically centered within its parent...

            * - :py:attr:`~CENTER`
              - When the X and Y position are both set to 0, this value places the center of the overlay at its parent's center. Increasing X values move the overlay to the right and increasing Y values move it up.

            * - :py:attr:`~CENTER_RIGHT`
              - When the X and Y position are both set to 0, this value places the right edge of the overlay at its parent's right edge and the center of the overlay is vertically centered within its parent...

            * - :py:attr:`~TOP_LEFT`
              - When the X and Y position are both set to 0, this value places the top, left corner of the overlay in its parent's top, left corner. Increasing X values move the overlay to the right and increasing Y values move it down.

            * - :py:attr:`~TOP_CENTER`
              - When the X and Y position are both set to 0, this value places the top edge of the overlay at its parent's top edge and the center of the overlay is horizontally centered within its parent...

            * - :py:attr:`~TOP_RIGHT`
              - When the X and Y position are both set to 0, this value places the top, right corner of the overlay in its parent's top, right corner. Increasing X values move the overlay to the left and increasing Y values move it down.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ScreenOverlayOrigin


