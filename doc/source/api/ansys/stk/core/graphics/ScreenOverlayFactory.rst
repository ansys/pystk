ScreenOverlayFactory
====================

.. py:class:: ansys.stk.core.graphics.ScreenOverlayFactory

   A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

.. py:currentmodule:: ScreenOverlayFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayFactory.initialize`
              - Initialize the overlay with the specified x position, y position, width, and height, all specified in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayFactory.initialize_with_position_and_size`
              - Initialize the overlay with the specified position and size.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ScreenOverlayFactory



Method detail
-------------

.. py:method:: initialize(self, xPixels: float, yPixels: float, widthPixels: float, heightPixels: float) -> IScreenOverlay
    :canonical: ansys.stk.core.graphics.ScreenOverlayFactory.initialize

    Initialize the overlay with the specified x position, y position, width, and height, all specified in pixels.

    :Parameters:

    **xPixels** : :obj:`~float`
    **yPixels** : :obj:`~float`
    **widthPixels** : :obj:`~float`
    **heightPixels** : :obj:`~float`

    :Returns:

        :obj:`~IScreenOverlay`

.. py:method:: initialize_with_position_and_size(self, position: list, size: list) -> IScreenOverlay
    :canonical: ansys.stk.core.graphics.ScreenOverlayFactory.initialize_with_position_and_size

    Initialize the overlay with the specified position and size.

    :Parameters:

    **position** : :obj:`~list`
    **size** : :obj:`~list`

    :Returns:

        :obj:`~IScreenOverlay`

