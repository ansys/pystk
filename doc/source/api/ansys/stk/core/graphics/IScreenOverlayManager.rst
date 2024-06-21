IScreenOverlayManager
=====================

.. py:class:: ansys.stk.core.graphics.IScreenOverlayManager

   object
   
   The top-level container for screen overlays. All child screen overlays that are added to this container are specified relative to the overall globe control.

.. py:currentmodule:: IScreenOverlayManager

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayManager.bounds`
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayManager.overlays`
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayManager.padding`
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayManager.display`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IScreenOverlayManager


Property detail
---------------

.. py:property:: bounds
    :canonical: ansys.stk.core.graphics.IScreenOverlayManager.bounds
    :type: list

    Gets the overall bounds of the globe control. The array contains the properties defining the bounds in the order left x location, top y location, width, height.

.. py:property:: overlays
    :canonical: ansys.stk.core.graphics.IScreenOverlayManager.overlays
    :type: IScreenOverlayCollection

    Gets the collection of overlays that are contained within this manager.

.. py:property:: padding
    :canonical: ansys.stk.core.graphics.IScreenOverlayManager.padding
    :type: list

    Gets or sets the padding surrounding the overlays that are contained within this manager. The array contains the components of the padding arranged in the order left, top, right, bottom.

.. py:property:: display
    :canonical: ansys.stk.core.graphics.IScreenOverlayManager.display
    :type: bool

    Gets or sets if the collection of overlays that are contained within this manager should be rendered.


