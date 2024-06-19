IScreenOverlayContainer
=======================

.. py:class:: IScreenOverlayContainer

   object
   
   The interface for screen overlays that contain a collection of other overlays. This interface is implemented by ScreenOverlayManager and ScreenOverlay.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~overlays`
            * - :py:meth:`~padding`
            * - :py:meth:`~display`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IScreenOverlayContainer


Property detail
---------------

.. py:property:: overlays
    :canonical: ansys.stk.core.graphics.IScreenOverlayContainer.overlays
    :type: IAgStkGraphicsScreenOverlayCollection

    Gets the collection of overlays that are contained within this overlay.

.. py:property:: padding
    :canonical: ansys.stk.core.graphics.IScreenOverlayContainer.padding
    :type: list

    Gets or sets the padding surrounding the overlays that are contained within this overlay. The array contains the components of the padding arranged in the order left, top, right, bottom.

.. py:property:: display
    :canonical: ansys.stk.core.graphics.IScreenOverlayContainer.display
    :type: bool

    Gets or sets if this overlay and the collection of overlays that are contained within this overlay should be rendered.


