ScreenOverlayPickResult
=======================

.. py:class:: ansys.stk.core.graphics.ScreenOverlayPickResult

   Describes a picked screen overlay as a result of a call to pick screen overlays.

.. py:currentmodule:: ScreenOverlayPickResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayPickResult.position`
              - Gets the position that was picked within the picked overlay. The array represents the picked position and has a size of 4. The elements are in the order x position, y position, x screen overlay unit, y screen overlay unit.
            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayPickResult.control_position`
              - Gets the position that was picked within the overall globe control. This is essentially the same position that was passed to pick screen overlays. The array represents the picked position and has a size of 4...
            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayPickResult.overlay`
              - Gets the screen overlay that was picked.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ScreenOverlayPickResult


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.graphics.ScreenOverlayPickResult.position
    :type: list

    Gets the position that was picked within the picked overlay. The array represents the picked position and has a size of 4. The elements are in the order x position, y position, x screen overlay unit, y screen overlay unit.

.. py:property:: control_position
    :canonical: ansys.stk.core.graphics.ScreenOverlayPickResult.control_position
    :type: list

    Gets the position that was picked within the overall globe control. This is essentially the same position that was passed to pick screen overlays. The array represents the picked position and has a size of 4...

.. py:property:: overlay
    :canonical: ansys.stk.core.graphics.ScreenOverlayPickResult.overlay
    :type: IScreenOverlay

    Gets the screen overlay that was picked.


