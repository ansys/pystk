ScreenOverlayManager
====================

.. py:class:: ansys.stk.core.graphics.ScreenOverlayManager

   Bases: :py:class:`~ansys.stk.core.graphics.IScreenOverlayCollectionBase`, :py:class:`~ansys.stk.core.graphics.IScreenOverlayContainer`

   The top-level container for screen overlays. All child screen overlays that are added to this container are specified relative to the overall globe control.

.. py:currentmodule:: ScreenOverlayManager

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayManager.bounds`
              - Get the overall bounds of the globe control. The array contains the properties defining the bounds in the order left x location, top y location, width, height.
            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayManager.display`
              - Get or set if the collection of overlays that are contained within this manager should be rendered.
            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayManager.overlays`
              - Get the collection of overlays that are contained within this manager.
            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayManager.padding`
              - Get or set the padding surrounding the overlays that are contained within this manager. The array contains the components of the padding arranged in the order left, top, right, bottom.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ScreenOverlayManager


Property detail
---------------

.. py:property:: bounds
    :canonical: ansys.stk.core.graphics.ScreenOverlayManager.bounds
    :type: list

    Get the overall bounds of the globe control. The array contains the properties defining the bounds in the order left x location, top y location, width, height.

.. py:property:: display
    :canonical: ansys.stk.core.graphics.ScreenOverlayManager.display
    :type: bool

    Get or set if the collection of overlays that are contained within this manager should be rendered.

.. py:property:: overlays
    :canonical: ansys.stk.core.graphics.ScreenOverlayManager.overlays
    :type: ScreenOverlayCollection

    Get the collection of overlays that are contained within this manager.

.. py:property:: padding
    :canonical: ansys.stk.core.graphics.ScreenOverlayManager.padding
    :type: list

    Get or set the padding surrounding the overlays that are contained within this manager. The array contains the components of the padding arranged in the order left, top, right, bottom.


