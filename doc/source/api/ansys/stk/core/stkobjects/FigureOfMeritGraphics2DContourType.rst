FigureOfMeritGraphics2DContourType
==================================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritGraphics2DContourType

   IntEnum


.. py:currentmodule:: FigureOfMeritGraphics2DContourType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~BLOCK_FILL`
              - Block Fill: color is applied to a region that contains points of a certain contour level.

            * - :py:attr:`~SMOOTH_FILL`
              - Smooth Fill: color is applied smoothly over all points in the grid to differentiate contour levels. NOTE: Not a valid choice when BoundsType (IAgCvGrid) is set to LatLine, LonLine or CustomBoundary.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritGraphics2DContourType


