CoverageGraphics2DAnimation
===========================

.. py:class:: ansys.stk.core.stkobjects.CoverageGraphics2DAnimation

   2D animation graphics options for the coverage grid.

.. py:currentmodule:: CoverageGraphics2DAnimation

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics2DAnimation.show_satisfaction`
              - Show Satisfaction: display graphics for regions of the grid that satisfy multiple figure of merit satisfaction criteria simultaneously during animation.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics2DAnimation.color`
              - Color of the animation graphics display.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics2DAnimation.fill_translucency`
              - Specify the fill translucency percentage for the animation graphics display. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageGraphics2DAnimation


Property detail
---------------

.. py:property:: show_satisfaction
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics2DAnimation.show_satisfaction
    :type: bool

    Show Satisfaction: display graphics for regions of the grid that satisfy multiple figure of merit satisfaction criteria simultaneously during animation.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics2DAnimation.color
    :type: agcolor.Color

    Color of the animation graphics display.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics2DAnimation.fill_translucency
    :type: float

    Specify the fill translucency percentage for the animation graphics display. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.


