IScreenOverlayContainer
=======================

.. py:class:: ansys.stk.core.graphics.IScreenOverlayContainer

   The interface for screen overlays that contain a collection of other overlays. This interface is implemented by ScreenOverlayManager and ScreenOverlay.

.. py:currentmodule:: IScreenOverlayContainer

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayContainer.overlays`
              - Gets the collection of overlays that are contained within this overlay.
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayContainer.padding`
              - Gets or sets the padding surrounding the overlays that are contained within this overlay. The array contains the components of the padding arranged in the order left, top, right, bottom.
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayContainer.display`
              - Gets or sets if this overlay and the collection of overlays that are contained within this overlay should be rendered.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IScreenOverlayContainer


Property detail
---------------

.. py:property:: overlays
    :canonical: ansys.stk.core.graphics.IScreenOverlayContainer.overlays
    :type: ScreenOverlayCollection

    Gets the collection of overlays that are contained within this overlay.

.. py:property:: padding
    :canonical: ansys.stk.core.graphics.IScreenOverlayContainer.padding
    :type: list

    Gets or sets the padding surrounding the overlays that are contained within this overlay. The array contains the components of the padding arranged in the order left, top, right, bottom.

.. py:property:: display
    :canonical: ansys.stk.core.graphics.IScreenOverlayContainer.display
    :type: bool

    Gets or sets if this overlay and the collection of overlays that are contained within this overlay should be rendered.


