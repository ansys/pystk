ICoverageGraphics2DAnimation
============================

.. py:class:: ICoverageGraphics2DAnimation

   object
   
   2D animation graphics options for the coverage grid.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_satisfaction_visible`
            * - :py:meth:`~color`
            * - :py:meth:`~fill_translucency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageGraphics2DAnimation


Property detail
---------------

.. py:property:: is_satisfaction_visible
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics2DAnimation.is_satisfaction_visible
    :type: bool

    Show Satisfaction: display graphics for regions of the grid that satisfy multiple figure of merit satisfaction criteria simultaneously during animation.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics2DAnimation.color
    :type: agcolor.Color

    Color of the animation graphics display.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics2DAnimation.fill_translucency
    :type: float

    Specify the fill translucency percentage for the animation graphics display. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.


