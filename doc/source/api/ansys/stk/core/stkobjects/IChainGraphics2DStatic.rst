IChainGraphics2DStatic
======================

.. py:class:: ansys.stk.core.stkobjects.IChainGraphics2DStatic

   object
   
   2D static graphics for a chain.

.. py:currentmodule:: IChainGraphics2DStatic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IChainGraphics2DStatic.is_visible`
              - Opt whether to have the 2D graphics window display complete chain access for objects in the chain, based on applicable time and object constraints. Accesses among chain objects are displayed as thick lines that overlay ground tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChainGraphics2DStatic.color`
              - Gets or sets the color in which chain graphics are displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChainGraphics2DStatic.line_width`
              - Gets or sets the width of the line that overlays the ground track in the 2D Graphics window.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IChainGraphics2DStatic


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DStatic.is_visible
    :type: bool

    Opt whether to have the 2D graphics window display complete chain access for objects in the chain, based on applicable time and object constraints. Accesses among chain objects are displayed as thick lines that overlay ground tracks.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DStatic.color
    :type: agcolor.Color

    Gets or sets the color in which chain graphics are displayed.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DStatic.line_width
    :type: LINE_WIDTH

    Gets or sets the width of the line that overlays the ground track in the 2D Graphics window.


