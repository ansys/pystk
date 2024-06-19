IFigureOfMeritGraphics
======================

.. py:class:: IFigureOfMeritGraphics

   object
   
   2D graphics for a Figure of Merit.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~static`
            * - :py:meth:`~animation`
            * - :py:meth:`~is_object_graphics_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGraphics


Property detail
---------------

.. py:property:: static
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics.static
    :type: IAgFmGfxAttributes

    Get the static graphics.

.. py:property:: animation
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics.animation
    :type: IAgFmGfxAttributesAnimation

    Get the animation graphics.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the Figure of Merit are visible.


