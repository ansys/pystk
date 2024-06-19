IScreenOverlayPickResult
========================

.. py:class:: IScreenOverlayPickResult

   object
   
   Describes a picked screen overlay as a result of a call to pick screen overlays.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~position`
            * - :py:meth:`~control_position`
            * - :py:meth:`~overlay`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IScreenOverlayPickResult


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.graphics.IScreenOverlayPickResult.position
    :type: list

    Gets the position that was picked within the picked overlay. The array represents the picked position and has a size of 4. The elements are in the order x position, y position, x screen overlay unit, y screen overlay unit.

.. py:property:: control_position
    :canonical: ansys.stk.core.graphics.IScreenOverlayPickResult.control_position
    :type: list

    Gets the position that was picked within the overall globe control. This is essentially the same position that was passed to pick screen overlays. The array represents the picked position and has a size of 4...

.. py:property:: overlay
    :canonical: ansys.stk.core.graphics.IScreenOverlayPickResult.overlay
    :type: IAgStkGraphicsScreenOverlay

    Gets the screen overlay that was picked.


