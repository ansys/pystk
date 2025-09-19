ScreenOverlayPinningOrigin
==========================

.. py:class:: ansys.stk.core.graphics.ScreenOverlayPinningOrigin

   IntEnum


.. py:currentmodule:: ScreenOverlayPinningOrigin

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~BOTTOM_LEFT`
              - When the X and Y pinning position are both set to 0, this value places the pinning position in the overlay's bottom, left corner. Increasing X values move the pinning position to the right and increasing Y values move it up.

            * - :py:attr:`~BOTTOM_CENTER`
              - When the X and Y pinning position are both set to 0, this value places the pinning position at its overlay's bottom edge and the pinning position is horizontally centered within its overlay...

            * - :py:attr:`~BOTTOM_RIGHT`
              - When the X and Y pinning position are both set to 0, this value places the pinning position in its overlay's bottom, right corner. Increasing X values move the pinning position to the left and increasing Y values move it up.

            * - :py:attr:`~CENTER_LEFT`
              - When the X and Y pinning position are both set to 0, this value places the pinning position at its overlay's left edge and the pinning position is vertically centered within its overlay...

            * - :py:attr:`~CENTER`
              - When the X and Y pinning position are both set to 0, this value places the pinning position at its overlay's center. Increasing X values move the pinning position to the right and increasing Y values move it up.

            * - :py:attr:`~CENTER_RIGHT`
              - When the X and Y pinning pinning position are both set to 0, this value places the pinning position at its overlay's right edge and the pinning position is vertically centered within its overlay...

            * - :py:attr:`~TOP_LEFT`
              - When the X and Y pinning position are both set to 0, this value places the pinning position in its overlay's top, left corner. Increasing X values move the pinning position to the right and increasing Y values move it down.

            * - :py:attr:`~TOP_CENTER`
              - When the X and Y pinning position are both set to 0, this value places the pinning position at its overlays's top edge and the pinning position is horizontally centered within its overlay...

            * - :py:attr:`~TOP_RIGHT`
              - When the X and Y pinning position are both set to 0, this value places the pinning position in its overlay's top, right corner. Increasing X values move the pinning position to the left and increasing Y values move it down.

            * - :py:attr:`~AUTOMATIC`
              - The pinning origin is automatically set to the origin of the overlay. For instance, if the origin of the overlay is ScreenOverlayOrigin.BottomLeft, the pinning origin will also be equivalent to ScreenOverlayPinningOrigin.BottomLeft.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ScreenOverlayPinningOrigin


